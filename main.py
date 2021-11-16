import uvicorn
# import multiprocessing

if __name__ == '__main__':
    # multiprocessing.freeze_support()
    uvicorn.run("app:app", host="0.0.0.0", port=44000, reload=True)
