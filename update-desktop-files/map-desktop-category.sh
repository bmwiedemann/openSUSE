#!/bin/bash

function mapCategory() {
  ret=""
  local in="${1#X-SuSE-}"
  case $in in
#old 9.0 Categories
    AddressBook)
       ret="ContactManagement"
       echo WARNING: AddressBook is an outdated Category, mapping it to ContactManagement
       ;;
    Camera)
       ret="Photography"
       echo WARNING: Camera is an outdated Category, mapping it to Photography
       ;;
    NewsReader)
       ret="News"
       echo WARNING: NewsReader is an outdated Category, mapping it to News
       ;;
    DialUp)
       ret="Dialup"
       echo WARNING: DialUp is an outdated Category, mapping it to Dialup
       ;;
    Telephone)
       ret="Telephony"
       echo WARNING: Telephone is an outdated Category, mapping it to Telephony
       ;;
    MidiPlayer)
       ret="Midi"
       echo WARNING: MidiPlayer is an outdated Category, mapping it to Midi
       ;;
    AudioMixer)
       ret="Mixer"
       echo WARNING: AudioMixer is an outdated Category, mapping it to Mixer
       ;;
    SimulationGame)
       ret="Simulation"
       echo WARNING: SimulationGame is an outdated Category, mapping it to Simulation
       ;;
    RolePlayingGame)
       ret="RolePlaying"
       echo WARNING: RolePlayingGame is an outdated Category, mapping it to RolePlaying
       ;;
    School)
       ret="Teaching"
       echo WARNING: School is an outdated Category, mapping it to Teaching
       ;;
    PuzzleGame)
       ret="LogicGame"
       echo WARNING: PuzzleGame is an outdated Category, mapping it to LogicGame
       ;;


#special cases
    Internet)
       ret="Network"
       echo WARNING: Internet is an illegal Category, mapping it to Network
       ;;
    DevelopmentWWW)
       ret="X-SuSE-WebDevelopment"
       echo WARNING: DevelopmentWWW is an illegal Category, mapping it to WebDevelopment
       ;;
    Language)
       ret="Languages"
       echo WARNING: Language is an illegal Category, mapping it to Languages
       ;;
    Burning)
       ret="DiscBurning"
       echo WARNING: Burning is an illegal Category, mapping it to DiscBurning
       ;;
    AudioVideoRecorder)
       ret="Recorder"
       echo WARNING: AudioVideoRecorder is an illegal Category, mapping it to Recorder
       ;;
    AudioVideoPlayer)
       ret="Player"
       echo WARNING: AudioVideoPlayer is an illegal Category, mapping it to Player
       ;;
    Photograph)
       ret="Photography"
       echo WARNING: Photograph is a mistyped Category, mapping it to Photography
       ;;
#Office Menu:
    Calendar|WordProcessor|Spreadsheet|ProjectManagement|Presentation| \
    Database|Dictionary|Finance|FlowChart|ContactManagement|PDFViewer) ret=$in ;;
    Warehouse|Addressbook)
       ret="X-SuSE-$in";;
#Internet/Network Menu:
    P2P|HamRadio|Email|News|Dialup|IRCClient|FileTransfer|InstantMessaging|WebBrowser|WebDevelopment|Feed) ret=$in ;;
    RSS-News)
       ret="X-SuSE-$in";;
#Development Menu:
    GUIDesigner|RevisionControl|IDE|Building|Debugger|Profiling|Translation) ret=$in ;;
    Design)
       ret="X-SuSE-$in";;
#Graphics Menu:
    3DGraphics|Photography|Scanning|OCR|VectorGraphics|RasterGraphics|2DGraphics|Maps| \
    Publishing|Viewer) ret=$in ;;
#Education and Science Menu:
    Teaching|Math|Chemistry|Astronomy|Art|Construction|Languages| \
    Engineering|Geography|Spirituality|Humanities|ArtificialIntelligence| \
    DataVisualization|Economy|Electricity|Geology|Geoscience|History|ImageProcessing| \
    Literature|MedicalSoftware|NumericalAnalysis|ParallelComputing|Physics|Robotics| \
    Sports|Biology) ret=$in ;;
#Multimedia Menu:
    AudioVideoEditing|Music|DiscBurning|Mixer|Player|Midi|Sequencer| \
    TV|Tuner|Recorder|Video) ret=$in ;;
    CD|CDReader|Jukebox)
       ret="X-SuSE-$in";;
#System Menu:
    Applet|Emulator|Monitor|Screensaver|TerminalEmulator|SystemSetup| \
    FileManager|Filesystem|Archiving|PackageManager|TrayIcon| \
    Security|RemoteAccess) ret=$in ;;
    ServiceConfiguration| \
    Backup|YaST|YaST-Hardware|YaST-Misc|YaST-Network|YaST-Virtualization|YaST-Support| \
    Feedback|YaST-Net_advanced|YaST-Security|YaST-Software|YaST-System|YaST-AppArmor|YaST-High_Availability)
       ret="X-SuSE-$in" ;;
#Utility Menu:
    Telephony|Accessibility|TextEditor|PDA|Calculator|Clock) ret=$in ;;
    DesktopUtility|SyncUtility|PrintingUtility|TimeUtility|WebUtility|Editor)
       ret="X-SuSE-$in" ;;
#Game Menu:
    3DGame|Amusement|ArcadeGame|CardGame|FirstPersonGame|BoardGame|\
    PlatformGame|PuzzleGame|SportsGame|StrategyGame|BlocksGame| \
    ActionGame|AdventureGame|KidsGame|LogicGame|Simulation|RolePlaying|Shooter)
       ret=$in ;;
#Control Center Categories:
    ControlCenter-Personal|ControlCenter-Hardware|ControlCenter-LookAndFeel|ControlCenter-System)
       ret="X-SuSE-$in" ;;
#XFCE Private Categories:
    X-Xfce*|X-XFCE*)
       ret="$in" ;;
#special tags:
    Application|Qt|KDE|GTK|GNOME|XFCE|Motif|ConsoleOnly|Shell|X-Red-*| \
    X-Ximian-*|X-GNOME-*|X-KDE-*|Settings|DesktopSettings|HardwareSettings| \
    Office|Network|Game|Graphics|Education|Documentation|Development| \
    Science|System|Utility|AudioVideo|AdvancedSettings|More) ret=$in ;;
    Core-Edutainment|Core-Game|Core-Graphics|Core-Internet| \
    Core-Multimedia|Core-Office|Core-Settings|Core-Utility|Core-System| \
    Core-Configuration|Core-Development|core)
       ret="X-SuSE-$in" ;;
    Core)
       ret="$in" ;;
    *) ret="" ;;
  esac
}
