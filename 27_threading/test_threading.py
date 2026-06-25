"""
Test untuk Threading vs Multiprocessing
"""
import time
import threading
import queue
import pytest
from concurrent.futures import ThreadPoolExecutor, as_completed
from main import io_task, download_file


class TestThreadingBasic:
    def test_io_task_returns_result(self):
        result = io_task("Test", 0.1)
        assert result == "Hasil Test"

    def test_thread_concurrent(self):
        """Test bahwa thread berjalan concurrent"""
        start = time.time()
        threads = []
        for i in range(3):
            t = threading.Thread(target=time.sleep, args=(0.5,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        # 3 threads x 0.5s = ~0.5s (concurrent), bukan 1.5s
        assert time.time() - start < 1.0


class TestThreadPoolExecutor:
    def test_map_results(self):
        def double(x):
            return x * 2

        with ThreadPoolExecutor(max_workers=2) as executor:
            results = list(executor.map(double, [1, 2, 3]))
        assert results == [2, 4, 6]

    def test_as_completed(self):
        def slow_add(x):
            time.sleep(0.1)
            return x + 1

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(slow_add, i) for i in range(3)]
            results = [f.result() for f in as_completed(futures)]
        assert sorted(results) == [1, 2, 3]


class TestLock:
    def test_counter_with_lock(self):
        counter = 0
        lock = threading.Lock()

        def increment(n):
            nonlocal counter
            for _ in range(n):
                with lock:
                    counter += 1

        threads = [threading.Thread(target=increment, args=(1000,)) for _ in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert counter == 5000


class TestQueue:
    def test_producer_consumer(self):
        q = queue.Queue()
        items = []

        def producer():
            for i in range(3):
                q.put(i)
            q.put(None)

        def consumer():
            while True:
                item = q.get()
                if item is None:
                    break
                items.append(item)

        prod = threading.Thread(target=producer)
        cons = threading.Thread(target=consumer)
        prod.start()
        cons.start()
        prod.join()
        cons.join()

        assert items == [0, 1, 2]


class TestDownloadManager:
    def test_download_file(self):
        result = download_file("https://example.com/test.zip")
        assert result["status"] == "OK"
        assert result["url"] == "https://example.com/test.zip"
        assert result["size"] > 0

    def test_concurrent_downloads(self):
        urls = ["https://example.com/f1.zip", "https://example.com/f2.zip"]
        start = time.time()

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(download_file, url) for url in urls]
            results = [f.result() for f in futures]

        assert len(results) == 2
        assert all(r["status"] == "OK" for r in results)
