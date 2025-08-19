from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt')

    model.train(
        data=r'..\data.yaml',
        epochs=110,
        imgsz=640,
        batch=16,
        device=0,
        workers=8,
        save_period=10
    )

if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()
    main()
