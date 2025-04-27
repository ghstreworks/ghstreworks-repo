import sys
import xbmcplugin
import xbmcgui

addon_handle = int(sys.argv[1])

xbmcplugin.setPluginCategory(addon_handle, 'GHSTreworks Trailery')
xbmcplugin.setContent(addon_handle, 'videos')

li = xbmcgui.ListItem(label='Trailer: Big Buck Bunny')
li.setInfo('video', {'title': 'Big Buck Bunny', 'genre': 'Animace'})
li.setProperty('IsPlayable', 'true')
xbmcplugin.addDirectoryItem(handle=addon_handle, url="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", listitem=li, isFolder=False)

xbmcplugin.endOfDirectory(addon_handle)
