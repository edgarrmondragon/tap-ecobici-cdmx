"""REST client handling, including EcobiciCDMXStream base class."""

from singer_sdk import RESTStream
from singer_sdk.authenticators import BearerTokenAuthenticator


class EcobiciCDMXStream(RESTStream):
    """Ecobici CDMX stream class."""

    url_base = "https://pubsbapi-latam.smartbike.com"

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Get an authenticator object.

        Returns:
            The authenticator instance for this REST stream.
        """
        token: str = self.config["token"]
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=token,
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        headers["User-Agent"] = f"{self.tap_name}/{self._tap.plugin_version}"
        return headers
