import multiprocessing as mp
import time

from PIL import Image



def resize_image(image_paths: list[str], queue: mp.Queue, event):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((800, 600))
        queue.put((image, image_path))
        # print("Размер изменен и картинка закинута в очередь")
    event.clear()


def recolor_image(queue: mp.Queue, event):
    while event.is_set() or not queue.empty():
        image, image_path = queue.get()
        image = image.convert("L")
        # print("Картинку достали из очереди")
        image.save(image_path)
        # print("Сохранили")


if __name__ == '__main__':

    event = mp.Event()
    event.set()

    paths = []
    queue = mp.Queue()

    for i in range(1, 1001):
        paths.append(f'Images\\img_{i}.jpg')


    start = time.time()
    resize_process = mp.Process(target=resize_image, args=(paths, queue, event))
    recolor_process = mp.Process(target=recolor_image, args=(queue, event))

    resize_process.start()
    recolor_process.start()

    resize_process.join()
    recolor_process.join()
    end = time.time()
    print(end - start)


# def refactor_image(image_paths):
#     for path in image_paths:
#         image = Image.open(path)
#         image = image.resize((800, 600))
#         image = image.convert("L")
#         image.save(path)
#
# paths = []
# for i in range(1, 1001):
#     paths.append(f"Images\\img_{i}.jpg")
#
# start = time.time()
# refactor_image(paths)
# end = time.time()
#
# print(end - start)