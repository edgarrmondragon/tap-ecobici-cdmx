"""Ecobici CDMX tap class."""

from typing import List, Type

from singer_sdk import Stream, Tap
from singer_sdk import typing as th
from singer_sdk.streams import RESTStream

from tap_ecobici_cdmx.streams import Stations, StationsStatus

STREAM_TYPES: List[Type[RESTStream]] = [
    Stations,
    StationsStatus,
]


class TapEcobiciCDMX(Tap):
    """Singer tap for Ecobici CDMX."""

    name = "tap-ecobici-cdmx"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "token",
            th.StringType,
            required=True,
            description="API Token for Ecobici CDMX",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Earliest datetime to get data from",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Ecobici CDMX streams.
        """
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
