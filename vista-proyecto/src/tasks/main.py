import logging
from prefect import flow


log = logging.getLogger()


@flow(name="LINKEDIN SCRAPPER")
def main_flow():
    log.info("PROCESO DE EXTRACCIÓN")


if __name__ == "__main__":
    main_flow()
