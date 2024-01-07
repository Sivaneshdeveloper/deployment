FROM python
WORKDIR __main__
COPY ./PG
CMD ["python3","__main__.py"]