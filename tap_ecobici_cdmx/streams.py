"""Stream type classes for tap-ecobici-cdmx."""

from singer_sdk import typing as th

from tap_ecobici_cdmx.client import EcobiciCDMXStream


class Stations(EcobiciCDMXStream):
    """Stations stream."""

    name = "stations"
    path = "/api/v1/stations.json"
    records_jsonpath = "$.stations[*]"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The station's unique identifier.",
        ),
        th.Property(
            "name",
            th.StringType,
            description="The station's name.",
        ),
        th.Property(
            "address",
            th.StringType,
            description="The station's address.",
        ),
        th.Property(
            "addressNumber",
            th.StringType,
            description="The station's address number.",
        ),
        th.Property(
            "zipCode",
            th.StringType,
            description="The station's zip code.",
        ),
        th.Property(
            "districtCode",
            th.StringType,
            description="The station's district code.",
        ),
        th.Property(
            "altitude",
            th.NumberType,
            description="The station's altitude.",
        ),
        th.Property(
            "nearbyStations",
            th.ArrayType(th.IntegerType),
            description="The station's nearby stations.",
        ),
        th.Property(
            "location",
            th.ObjectType(
                th.Property("lat", th.NumberType),
                th.Property("lon", th.NumberType),
            ),
            description="The station's location.",
        ),
        th.Property(
            "stationType",
            th.StringType,
            description="The station's type.",
        ),
    ).to_dict()


class StationsStatus(EcobiciCDMXStream):
    """Stations status stream."""

    name = "stations_status"
    path = "/api/v1/stations/status.json"
    records_jsonpath = "$.stationsStatus[*]"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.IntegerType,
            description="The station's unique identifier.",
        ),
        th.Property(
            "status",
            th.StringType,
            description="The station's status.",
        ),
        th.Property(
            "availability",
            th.ObjectType(
                th.Property("bikes", th.IntegerType),
                th.Property("slots", th.IntegerType),
            ),
            description="The station's bike availability.",
        ),
    ).to_dict()
