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

VPN-Sentinel can emit a sound when the VPN link becomes inactive.

VPN-Sentinel allows you, as soon as it starts, to automatically connect to the last VPN you used, if you wish.

Events concerning the VPN as well as the applications concerned can be logged.

A hotkey can be set for connecting to the last VPN used and disconnecting. (Alt+V by default.)

VPN-Sentinel can manage each of the Internet applications: possibility of automatic start when a VPN is active, stop when it becomes inactive, stop after a few seconds if no VPN is active.

## Settings

The VPN-Sentinel Settings are accessible via its contextual menu (right click on its icon).

Four tabs are available:

  - **Notifications**
    * Flag
      * Whether or not to display the VPN server's country flag next to the icon?
    * Sound Alert
      * Whether or not to emit a sound alert when VPN link becomes idle?
    * Icon Colors
  - **VPN**
    * Connection Policy
    * Activity Log
  - **Flags**
    * Flag list
  - **VPN-related Apps**

