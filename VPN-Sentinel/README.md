# VPN-Sentinel

## Summary

VPN-Sentinel is a Cinnamon applet that replaces VPN-LookOut.

VPN-Sentinel monitors the stability of your **Wireguard** and **VPN** links, and acts according to the security policy you have chosen.

(Hereafter, "VPN" also includes Wireguard.)

## Types of VPNs Successfully Tested with VPN-Sentinel

| Type of VPN | VPN-Sentinel version |
|-------------|----------------------|
|Wireguard    | >= 1.0.0             |
|OpenVPN      | >= 1.0.0             |
|L2TP         | >= 1.0.0             |
|PPTP         | >= 1.0.0             |

If you have successfully tested other types of VPNs, please let the Author know and explain how to install and configure them.

## Features

VPN-Sentinel displays an icon whose color changes depending on the status of the VPN link (connected, disconnected, transient); you can choose these colors.

The flag of the country where the VPN server you are connected to is located can be displayed next to the icon.

When hovering over or clicking on the icon, the following information is displayed: the name of the VPN, the interface used, the time (and possibly the date) since which the link has been active.

