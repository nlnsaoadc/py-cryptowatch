from unittest import TestCase, mock

from cryptowatch import Cryptowatch


class CryptowatchTestCase(TestCase):
    def setUp(self):
        self.api = Cryptowatch(key="123test")

    def test_get_headers(self):
        headers = self.api._get_headers()
        self.assertIsNotNone(headers["X-CW-API-Key"])

    @mock.patch(
        "requests.get", return_value=mock.Mock(status_code=200, json=lambda: {})
    )
    def test_get(self, mock_get):
        self.api._get("test")
        mock_get.assert_called_once_with(
            url="https://api.cryptowat.ch/test",
            headers={"X-CW-API-Key": "123test"},
            params=None,
        )

    @mock.patch("cryptowatch.cryptowatch.logger.warning")
    @mock.patch(
        "requests.get",
        return_value=mock.Mock(
            status_code=404,
            json=lambda: {"message": "Not Found"},
            content=b"404 Not Found Message",
        ),
    )
    def test_get_404_status(self, mock_get, mock_log):
        with self.assertRaises(Exception) as context:
            self.api._get("test")
        self.assertEqual(
            "404 404 Not Found Message",
            str(context.exception),
        )
        mock_log.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.logger.info")
    @mock.patch(
        "requests.get",
        return_value=mock.Mock(
            status_code=404,
            json=mock.Mock(side_effect=Exception("")),
            content=b"404 Not Found Message",
        ),
    )
    def test_get_404_status_fail_silently(self, mock_get, mock_log):
        self.api.fail_silently = True
        self.assertEqual(self.api._get("test"), None)
        mock_log.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_assets(self, mock_get):
        self.api.get_assets()
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_asset(self, mock_get):
        self.api.get_asset(symbol="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_pairs(self, mock_get):
        self.api.get_pairs()
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_pair(self, mock_get):
        self.api.get_pair(pair="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_markets(self, mock_get):
        self.api.get_markets()
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_market(self, mock_get):
        self.api.get_market(exchange="", pair="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_market_price(self, mock_get):
        self.api.get_market_price(exchange="", pair="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_market_prices(self, mock_get):
        self.api.get_market_prices()
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_market_trades(self, mock_get):
        self.api.get_market_trades(exchange="", pair="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_market_summary(self, mock_get):
        self.api.get_market_summary(exchange="", pair="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_market_summaries(self, mock_get):
        self.api.get_market_summaries()
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_order_book(self, mock_get):
        self.api.get_order_book(exchange="", pair="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_order_book_liquidity(self, mock_get):
        self.api.get_order_book_liquidity(exchange="", pair="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_order_book_calculator(self, mock_get):
        self.api.get_order_book_calculator(exchange="", pair="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_ohlc(self, mock_get):
        self.api.get_ohlc(exchange="", pair="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_exchanges(self, mock_get):
        self.api.get_exchanges()
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_exchange(self, mock_get):
        self.api.get_exchange(exchange="")
        mock_get.assert_called_once()

    @mock.patch("cryptowatch.cryptowatch.Cryptowatch._get")
    def test_get_exchange_markets(self, mock_get):
        self.api.get_exchange_markets(exchange="")
        mock_get.assert_called_once()
