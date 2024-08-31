# captive-portal

[![GitHub license](https://img.shields.io/github/license/Zedeldi/captive-portal?style=flat-square)](https://github.com/Zedeldi/captive-portal/blob/master/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/Zedeldi/captive-portal?style=flat-square)](https://github.com/Zedeldi/captive-portal/commits) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

Proof-of-concept captive portal credential harvester using `create_ap` and Flask.

## Description

Creates an open Wi-Fi access point, which redirects all traffic to localhost, using `create_ap`, which in turn uses `hostapd` and `dnsmasq`.
A Flask web server is hosted on the AP gateway, which serves a login page.
Received credentials are stored in a CSV file, `creds.csv` by default.
DNS requests and AP logs are saved in `dnsmasq.log` and `create_ap.log`, respectively.

The AP never actually provides internet access; all requests are always redirected to localhost, returning a login page.
This may reveal that the access point is rogue or appear as though the network is misconfigured.
The access point could be modified to allow traffic through once credentials have been received, but this is outside of the scope for this project.

The logo displayed at the top of the login page is stored at `static/images/logo.png`.
Changing this to a trusted company logo can improve the efficacy of the attack, and make the login page look more legitimate.

## Disclaimer

This project was created to demonstrate how a social engineering attack can exploit the greatest vulnerability in all systems: the user.
Education and training is the best mitigation for these attacks.
One way to achieve this is by sharing how and why these methods work.

Please use this software responsibly and for demonstration/educational purposes only.

## Usage

1. Clone the repository with: `git clone https://github.com/Zedeldi/captive-portal.git`
2. Change directory to the cloned repository: `cd captive-portal`
3. Ensure the required [dependencies](#dependencies) are installed/accessible
4. Run `portal-start` as root: `sudo ./portal-start`

Please note that `NetworkManager` will be stopped automatically.
If the configured NIC is managed by another application, the relevant service may need to be stopped manually to prevent interference with `create_ap`.

### Dependencies

- [linux-wifi-hotspot](https://github.com/lakinduakash/linux-wifi-hotspot) - Wi-Fi hotspot
- [Flask](https://pypi.org/project/Flask/) - HTTP interface
  - [Bootstrap](https://getbootstrap.com/) - CSS framework (bundled)
  - [Feather](https://feathericons.com/) - default logo (bundled)

## License

`captive-portal` is licensed under the [MIT Licence](https://mit-license.org/) for everyone to use, modify and share freely.

This project is distributed in the hope that it will be useful, but without any warranty.

## Donate

If you found this project useful, please consider donating. Any amount is greatly appreciated! Thank you :smiley:

[![PayPal](https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-150px.png)](https://paypal.me/ZackDidcott)
