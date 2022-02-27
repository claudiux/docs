# Radio3.0 - Manual

## Author: Claudiux (@claudiux on Github)

### Last revision date: 27/02/2022

***

## Overview

Radio3.0 is an *Internet Radio Receiver & Recorder* applet for Cinnamon.


With Radio3.0 you can:

  * Listen thousands of internet radios.

  * Record songs or programs while listening to them.

  * Manage your list of favorite radios: add, move, remove, modify each radio of your list.

  * Create categories and sort yourself your favorite radios.

  * Save and restore entire lists of radios.

![Screenshots of Menu and Contextual menu][screenshot]{ width=600px }

***

## Table of contents

  1. [Dependencies](#Dependencies)

  1. [Manual installation of the dependencies](#DepManualInstall)  
      1. [Linux Mint, Ubuntu, Debian](#DepMint)  
      1. [Arch](#DepArch)  
      1. [Fedora](#DepFedora)  

  1. [How to install the Radio3.0 applet?](#InstallApplet)  
    1. [Using the Cinnamon System Settings](#InstallAppletCS)  
    1. [Using the SpicesUpdate applet](#InstallAppletSU)  

  1. [Where to place the Radio3.0 applet icon?](#WhereToPlace)

  1. [Using the Radio3.0 applet](#UsingApplet)  
    1. [How to add radio stations to my list?](#HowToAdd)  
    1. [Listen a radio](#ListenRadio)  
    1. [Listen the last radio listened to](#ListenLastRadio)  
    1. [Listen at Cinnamon startup the last radio you listened to](#ListenAtStartup)  
    1. [Stop the radio](#StopRadio)  
    1. [Set the volume of the radio stream](#SetVolume)  
    1. [Manage the list of my radios](#ManageRadios1)  
    1. [Recording a song or a radio program](#RecordingSong)  
    1. [Open the folder containing my recordings](#OpenRecFolder)  
    1. [Modify my recordings](#ModifyRecords)  

  1. [Settings](#Settings)  
    1. [Radios](#RadiosTab)  
        1. [Stations and Categories on the menu](#RadiosTabStations)  
        1. [Moving selected stations/categories](#RadiosTabMoving)  
        1. [Save and restore](#RadiosTabSaveRestore)  
        1. [Update your list using the Radio Database](#RadiosTabUpdate)  
    1. [Search](#SearchTab)  
    1. [Import](#ImportTab)  
    1. [Menu](#MenuTab)  
    1. [Network](#NetworkTab)  
    1. [Behavior](#BehaviorTab)  
    1. [Recording](#RecordingTab)  

***
<a name="Dependencies"></a>
## Dependencies

Radio3.0 uses:

  * _mpv_ (an efficient Media Player) to play the radio streams.

  * _sox_ (Sound eXchange) to record in a file the radio stream, or rather the sound coming out of your sound card.

  * _pacmd_ (PulseAudio Command) which is a _pulseaudio_ tool.

  * _at_ to schedule recordings.

  * _libnotify-bin_ to display notifications.

  * _youtube-dl_ to download videos from YT.

  * _ffmpeg_ and _ffmpegthumbnailer_ to extract the soundtrack from the downloaded video.

  * _python3-polib_ to install translations, when exist.

If the packages containing these tools are not already installed, you are prompted to do so when using Radio3.0 for the first time.

You can also install _Pulse Effects_ to use several sound effects (reverb, etc.). But this is optional.

<a name="DepManualInstall"></a>
## Manual installation of the dependencies

<a name="DepMint"></a>
### Linux Mint, Ubuntu, Debian

`sudo apt-get update`

`sudo apt-get install mpv libmpv1 libmpv-dev sox libsox-fmt-all pulseaudio pulseaudio-utils at libnotify-bin youtube-dl ffmpeg ffmpegthumbnailer python3-polib`

Optionally:

`sudo apt-get install pulseeffects`

<a name="DepArch"></a>
### Arch

`sudo pacman -Syu mpv sox pulseaudio at libnotify youtube-dl ffmpeg ffmpegthumbnailer`

<a name="DepFedora"></a>
### Fedora

`sudo dnf install mpv sox pulseaudio at libnotify youtube-dl ffmpeg gstreamer1-libav`

<a name="InstallApplet"></a>
## How to install the Radio3.0 applet?

<a name="InstallAppletCS"></a>
### Using the Cinnamon System Settings

Right-click on a panel -> Applets -> Download tab: Download Radio3.0. Then switch on the Manage tab and add Radio3.0 to the panel.

<a name="InstallAppletSU"></a>
### Using the SpicesUpdate applet

In the SpicesUpdate menu, select Applets. Download the latest version of Radio3.0. Then switch on the Manage tab and add Radio3.0 to a panel.

<a name="WhereToPlace"></a>
## Where to place the Radio3.0 applet icon?

The best place is near the _Sound_ applet. So you can easily control the general volume with the _Sound_ applet and the radio volume with the Radio3.0 applet.

(To move applets, use the "Panel edit mode" in the contextual menu of a panel. Exit this "Panel edit mode" when your applet icons are at their right place.)

<a name="UsingApplet"></a>
## Using the Radio3.0 applet

This applet has a menu (left-click) and a contextual menu (right-click).

Some actions can be made using middle-click or scrolling on the icon.

<a name="HowToAdd"></a>
### How to add radio stations to my list?
There are three ways to add at least one radio station in your list.

  1. In the menu, select the "Search for new stations..." option. (You also can use the "Configure..." option in the contextual menu, then select the "Search" tab.) Use the form to query the internet database containing several tens of thousands of references.

  1. You can import files containing radio station data, using the "Import" tab (with the same "Configure..." option of the contextual menu).

  1. You can directly add a radio station to your list, if you know its stream URL. Your list is in the "Radios" tab (the first tab opened when you select "Configure..."). Only the "Name" and "Stream URL" fields are required; the others are optional.

Each of these tabs contains some explanations for using it. These can be skipped by unchecking the appropriate box in the "Behavior" tab.

<a name="ListenRadio"></a>
### Listen to a radio

  * Open the menu of Radio3.0 (clicking on its icon).

  * Open the sub-menu "All my radios".

  * Select a radio station and wait some seconds. The waiting time depends on the distance that separates you from the stream server and the quality of this stream.

Please note that the last radio stations selected appear in the "Recent" part of the menu to give them quick access.

While listening a radio, the color of the symbolic icon changes (green by default; you can select another color).

<a name="ListenLastRadio"></a>
### Listen the last radio listened to

While no radio is playing, middle-click on the icon.

(Another way : Click on the first radio in the Recent section of the menu.)

<a name="ListenAtStartup"></a>
### Listen at Cinnamon startup the last radio you listened to

Check the "Radio ON at startup" option in the contextual menu.

<a name="StopRadio"></a>
### Stop the radio

There are two ways to stop the radio:

  * Click on Stop in the menu.

  * Middle-click on the icon.

While radio is OFF, the color of the symbolic is the default one (gray by default; you can select another color).

<a name="SetVolume"></a>
### Set the volume of the radio stream

Scrolling up or down on the icon adjusts the volume of the current radio stream.

Using the volume slider in the contextual menu has the same effect.

Please note that these actions have no effects on the general volume; use the icon of the _Sound_ applet to adjust the general volume.

<a name="ManageRadios1"></a>
### Manage the list of my radios

Select Configure... in the menu or in the contextual menu to access to the settings (see [below](#RadiosTab)).

<a name="RecordingSong"></a>
### Recording a song or a radio program

<u>Condition</u>: Check the box in the Consent section of the Recordings tab in this applet's settings.

<u>First way</u>: Select _Start Recording_ in the contextual menu.

<u>Second way</u>: Click on the _Record this!_ button of the notification while it appears on the screen. Hovering the mouse over this button allows you to wait for the start of the song without the notification disappearing. If the notification disappears before you can click this button, you will need to use the Start recording option from the contextual menu.

This second way depends on the ability of your stream to give the title of the song or program.

While recording, the color of the symbolic icon changes (red by default; you can select another color).

<u>Please note</u>:

  * If the radio stream give the title of the song or program, then the recording will automatically stop at the end of this song or program. Watch out for the advertising breaks announced in the stream!

  * Otherwise you will have to stop recording yourself.

<a name="OpenRecFolder"></a>
### Open the folder containing my recordings

In the contextual menu: Open Recordings Folder.

<a name="ModifyRecords"></a>
### Modify my recordings

You can use an external program like Audacity to modify your recordings.

<a name="Settings"></a>
## Settings

Settings are accessible from the menu or from the contextual menu using the _Configure..._ option.

![Settings Tabs][sshot_settings_tabs]{ width=600px }

There are 8 tabs in the Radio3.0 Settings:

| [Radios](#RadiosTab) | [Search](#SearchTab) | [Import](#ImportTab)| [Menu](#MenuTab)| [Behavior](#BehaviorTab)| [Network](#NetworkTab)| [Recording](#RecordingTab)| [Scheduling](#SchedulingTab)|
|----------------------|----------------------|---------------------|-----------------|-------------------------|-----------------------|---------------------------|-----------------------------|



<a name="RadiosTab"></a>
### Radios

<a name="RadiosTabStations"></a>
#### Stations and Categories on the menu

![Radios Settings Screenshot][sshot_radios_tab1]{ width=670px }

This is an example of radio stations list.

Three Categories are visible: **Hard Rock & Metal**, **Reggae** and **Techno / Dance**. They have their Streaming URL empty.

All the others are radio stations. Those whose **Menu** box is checked appear in the menu of this applet (in the My Radio Stations sub-menu; see below). Those whose **♪/➟** box is checked can be immediately played (one after the other) using the **♪ Play the next station to test** button.

Each Category or Station can be moved using **drag-and-drop**.

Below this list, the left part contains **tools** to modify the contents of the list:

  * ![Plus button][plus_button]{ align=middle ; width=30px } to **add** a Category (only fill in its name) or Station (fill in at least its name and its streaming URL). The added item is at the very top of the list.

  * ![Minus button][minus_button]{ align=middle ; width=30px } to **remove** the selected item. (You select an item by clicking on it.)

  * ![Pencil button][pencil_button]{ align=middle ; width=30px } to **edit** the selected item.

  * ![Unchecked button][unchecked_button]{ align=middle ; width=30px } to **unselect** any item.

  * ![Move up button][moveup_button]{ align=middle ; width=30px } to **move up** the selected item.

  * ![Move down button][movedown_button]{ align=middle ; width=30px } to **move down** the selected item.

The right part contains tools to explore your list:

  * ![Top button][top_button]{ align=middle ; width=30px } to go to the **top** of your list.

  * ![Move up button][moveup_button]{ align=middle ; width=30px } to go to the **previous page**.

  * ![Move down button][movedown_button]{ align=middle ; width=30px } to go to the **next page**.

  * ![Bottom button][bottom_button]{ align=middle ; width=30px } to go to the **bottom** of your list.

  * ![Previous Category button][prevcat_button]{ align=middle ; width=30px } to go to the **previous Category**.

  * ![Next Category button][nextcat_button]{ align=middle ; width=30px } to go to the **next Category**.

![Sub-menu My Radio Stations][sshot_menu_myradiostations]{ width=350px }

<a name="RadiosTabMoving"></a>
#### Moving selected stations/categories

![Radios Settings Screenshot 2][sshot_radios_tab2]{ width=670px }

To change the category of certain items, select them by checking their **♪/➟** box, choose the category from the drop-down list and click on the "Move selected stations to this category" button.

To see the result and make any adjustments, then click on "Go to this category".

Tip: You can create a temporary category and move it to the right place, then move those selected items to that category before deleting it.

<a name="RadiosTabSaveRestore"></a>
#### Save and restore

![Radios Settings Screenshot 3][sshot_radios_tab3]{ width=670px }

**Save** (backup) your list of stations before editing or updating it. This creates a `.json` file containing all the details of your stations and categories. The name of this `.json` file describes the date and time of the backup; example: `Radios_2022-02-21_22-23-55.json` was created on February 21, 2022 at 10:23:55 p.m.

**Restore** a previously saved station list.Beware: Your list will be entirely replaced by the restored list.

By opening the folder containing these lists, you can manage them. In particular, you can rename them at your convenience.

<a name="RadiosTabUpdate"></a>
#### Update your list using the Radio Database

![Radios Settings Screenshot 4][sshot_radios_tab4]{ width=670px }

The purpose of the button **Update my station list with the Radio Database data** is to complete the empty fields of your radios as much as possible.

If the consulted database contains the streaming URL that you have declared for a station, then a UUID (Universal Unique IDentifier)  will be assigned to this station.

If one of your stations is no longer reachable, try updating your list. This station's broadcast URL may have changed and if it has a UUID, its new URL may be assigned to it.

An update will not change the name you have given to a station.

Notes:

  * If a station comes from the database (Search tab), it already has a UUID.

  * If it comes from another source, it may be unknown to the database; it will then not be assigned a UUID.


<a name="SearchTab"></a>
### Search

#### Search form

![Search Form Screenshot][sshot_search_tab1]{ width=670px }

Filling in at least a few fields of this form then clicking on the 'Search ...' button you can search for other stations in a free radio database accessible via the Internet.

Each time the 'Search ...' button is clicked, a new results page is displayed in the second part of this tab, where you can test certain stations and include them in the menu.

A station already in your menu will only appear in search results if its streaming URL has changed.

When no new page appears, it means that all results matching your search criteria have been displayed.

If you modify at least one of your criteria, remember to set the 'Next page number' field to 1.

As usual, the 'Reset' button resets every field on this form to its default value.

#### Search results

To obtain these results, the search form was reset and then filled with:

  - Tag: metal
  - Codec: AAC
  - Order: bitrate

![Search Results Screenshot][sshot_search_tab2]{ width=700px }

To test 'TheBlast.fm', check its **♪** box then click on the **♪ Play the next station to test** button. Please note: testing a radio station adds it to the "Recently Played Stations" in this applet menu, but does not add it to your station list.



<a name="ImportTab"></a>
### Import

<a name="MenuTab"></a>
### Menu

<a name="BehaviorTab"></a>
### Behavior

![Behavior Settings Screenshot][sshot_behavior_settings]{ width=700px }

<a name="NetworkTab"></a>
### Network

![Network Settings Screenshot][sshot_network_settings]{ width=700px }

<a name="RecordingTab"></a>
### Recording

![Recording Settings Screenshot][sshot_recording_settings]{ width=700px }

<a name="SchedulingTab"></a>
### Scheduling


[screenshot]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/screenshot.png
[sshot_settings_tabs]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_Settings_All_Tabs.png
[sshot_radios_tab1]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_RadiosTab_1.png
[sshot_radios_tab2]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_RadiosTab_2.png
[sshot_radios_tab3]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_RadiosTab_3.png
[sshot_radios_tab4]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_RadiosTab_4.png
[plus_button]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_Plus_button.png
[minus_button]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_Minus_button.png
[pencil_button]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_Pencil_button.png
[unchecked_button]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_Unchecked_button.png
[moveup_button]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_MoveUp_button.png
[movedown_button]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_MoveDown_button.png
[top_button]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_Top_button.png
[bottom_button]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_Bottom_button.png
[prevcat_button]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_PrevCat_button.png
[nextcat_button]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_NextCat_button.png
[sshot_menu_myradiostations]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_Menu_MyRadioStations.png  "My Radio Stations"

[sshot_search_tab1]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_SearchTab_1.png
[sshot_search_tab2]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_SearchTab_2.png

[sshot_behavior_settings]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_BehaviorSettings.png
[sshot_recording_settings]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_RecordingSettings.png
[sshot_network_settings]: https://github.com/claudiux/docs/raw/master/Radio3.0/screenshots/Radio30_NetworkSettings.png
