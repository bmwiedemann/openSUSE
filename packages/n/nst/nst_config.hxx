#pragma once

// C++
#include <array>
#include <chrono>
#include <set>
#include <string_view>

// xpp
#include "xpp/keyboard.hxx"
#include "xpp/types.hxx"
#include "xpp/XCursor.hxx"

// nst
#include "fwd.hxx"
#include "Selection.hxx"
#include "themes.hxx"
#include "types.hxx"

namespace nst::config {

/// Default character font to use.
/**
 * \see http://freedesktop.org/software/fontconfig/fontconfig-user.html
 **/
constexpr std::string_view FONT{"Liberation Mono:pixelsize=12:antialias=true:autohint=true"};
/// Font default pixel size to use, if not specified in FONT
constexpr double FONT_DEFAULT_SIZE_PX = 12;

/// Word delimiter string for expanding selection upon double/triple clicking
/**
 * More advanced example: L" `'\"()[]{}"
 **/
inline constexpr const std::wstring_view WORD_DELIMITERS{L" \"<>()[]'{}:/"};

/// How stty will be invoked when operating on real TTY lines.
constexpr std::array<std::string_view, 8> STTY_ARGS{{
	"stty", "raw", "pass8", "nl", "-echo", "-iexten", "-cstopb", "38400"
}};

/// The default command to invoke for when the "open_buffer_in_editor" keyboard shortcut is executed.
const std::vector<std::string> EXTERNAL_PIPE_CMDLINE{"gvim", "--not-a-term", "-"};

/*
 * What program is executeed by nst depends on these precedence rules:
 * 1: program passed with -e
 * 2: scroll and/or utmp
 * 3: SHELL environment variable
 * 4: value of shell in /etc/passwd
 * 5: value of SHELL in here
 */

/// Shell to execute if none found in environment or on command line
constexpr std::string_view SHELL{"/bin/sh"};
constexpr std::string_view UTMP{};
/// Scroll program: to enable use a string like "scroll"
constexpr std::string_view SCROLL{};
/// Default TERM value
constexpr std::string_view TERM_NAME{"nst-256color"};

/// Identification sequence returned in DA and DECID escape sequences
constexpr std::string_view VT_IDENT{"\033[?6c"};

/// Allow certain non-interactive (insecure) window operations such as setting the clipboard text
constexpr bool ALLOW_WINDOW_OPS = false;

/// Spaces per tab.
/**
 * When you are changing this value, don't forget to adapt the »it« value in
 * the nst.info and appropriately install the nst.info in the environment where
 * you use this nst version.
 *
 *	it#$TABSPACES,
 *
 * Secondly make sure your kernel is not expanding tabs. When running `stty
 * -a` »tab0« should appear. You can tell the terminal to not expand tabs by
 *  running following command:
 *
 *	stty tabs
 */
constexpr int TABSPACES = 8;

/// Allow alternative screen usage
constexpr bool ALLOW_ALTSCREEN = true;

/// Number of border pixels between window frame and actual terminal characters
constexpr int BORDERPX = 2;

/* Kerning / character bounding-box multipliers */
constexpr float CW_SCALE = 1.0;
constexpr float CH_SCALE = 1.0;

/// Double click selection timeout.
constexpr std::chrono::milliseconds DOUBLE_CLICK_TIMEOUT{300};

/// Automatically clear selection when selection ownership is lost.
/**
 * Set this to true if you want the selection to disappear when you select
 * something different in another window.
 **/
constexpr bool SEL_CLEAR = false;

/// Keep trailing newlines in Selection::Flag::LINES style selections.
/**
 * When selecting a range of full lines, keep trailing newlines. Upon
 * pasting this causes a final newline to be pasted, as well. This can be
 * undesirable when pasting e.g. a single line in a shell prompt (which you
 * want to edit, before executing it).
 *
 * If disabled then trailing newline characters will be skipped during
 * pasting.
 **/
constexpr bool LINE_PASTE_KEEP_NEWLINE = false;

/// Minimum draw latency.
/*
 * Time from new content/keypress/etc until drawing.
 *
 * Within this range, nst draws when content stops arriving (idle). mostly
 * it's near MINLATENCY, but it waits longer for slow updates to avoid partial
 * draw.  low MINLATENCY Will tear/flicker more, as it can "detect" idle too
 * early.
 */
constexpr std::chrono::milliseconds MIN_LATENCY{8};
/// Maximum draw latency.
/**
 * \see MIN_LATENCY
 **/
constexpr std::chrono::milliseconds MAX_LATENCY{33};

/// Blinking timeout.
/**
 * Set to 0 to disable blinking. This is used for the terminal blinking
 * attribute.
 **/
constexpr std::chrono::milliseconds BLINK_TIMEOUT{800};

/// Thickness of bar style cursors.
constexpr int CURSOR_THICKNESS = 2;

/// Terminal bell volume.
/**
 * It must be a value between -100 and 100. Use 0 for disabling it.
 **/
constexpr xpp::BellVolume BELL_VOLUME{0};

/// Default colors to use, see themes.hxx for available themes.
const auto THEME = DEFAULT_THEME;

/// Default shape of cursor
constexpr CursorStyle CURSORSHAPE = CursorStyle::STEADY_BLOCK;

/// Default number of columns.
constexpr unsigned int COLS = 80;
/// Default number of rows.
constexpr unsigned int ROWS = 24;
/// Number of lines kept in the scrollback buffer.
constexpr size_t HISTORY_LEN = 10000;
/// Whether nst should keep a selected scrollback position even when new TTY data comes in.
/**
 * When the terminal history is displayed then the question arises what to do
 * when new TTY data comes in from the shell or another running process. If
 * this is set to `true` then nst will keep the scrolled-to position until
 * either
 *
 * - an interactive keyboard / mouse event occurs (except for scrollback
 *   control).
 * - the history buffer is full and overwritten by new data, in which case nst
 *   will scroll to the oldest available history data.
 *
 * If set to `false` then nst will jump back to the current screen in these
 * cases. Like this also includes window resize events, if the active program
 * (e.g. the shell) reacts to the event and changes terminal content. You can
 * still stop the terminal process via Ctrl + S to prevent any new output to
 * appear.
 **/
constexpr bool KEEP_SCROLL_POSITION = true;

/// Whether nst should offer a UNIX domain socket IPC for the nst-msg tool.
/**
 * If enabled then a UNIX domain listen socket is created for each nst
 * instance. The `nst-msg` utility can be used to talk to the terminal for
 * obtaining terminal history contents e.g. for grepping on it.
 **/
constexpr bool ENABLE_IPC = true;

/// Default shape of the mouse cursor.
constexpr xpp::CursorFont MOUSE_SHAPE{xpp::CursorFont::XTERM};
/// Default foreground color of the mouse cursor.
constexpr ColorIndex MOUSE_FG{7};
/// Default background color of the mouse cursor.
constexpr ColorIndex MOUSE_BG{0};
/// If set then the mouse cursor in will be hidden from the terminal window when typing.
constexpr bool HIDE_MOUSE_CURSOR = true;

/// Fallback color to use if no matching font is found.
/**
 * Color used to display font attributes when fontconfig selected a font which
 * doesn't match the ones requested.
 **/
constexpr ColorIndex DEFAULT_ATTR{11};

/// Input modifier mask which forces mouse select/shortcuts in WinMode::MOUSE.
/**
 * Force mouse select/shortcuts while mask is active (when MODE_MOUSE is set).
 * Note that if you want to use ShiftMask with selmasks, set this to an other
 * modifier, set to InputModifier::NONE to not use it.
 **/
constexpr xpp::InputMask FORCE_MOUSE_MOD{xpp::InputModifier::SHIFT};

// shorthands for shorter definitions below
using KeyID     = xpp::KeySymID;
using Mod       = xpp::InputModifier;
using Mask      = xpp::InputMask;
using AppKey    = Key::AppKeypad;
using AppCursor = Key::AppCursor;

/// Modifier state to ignore when matching key or button events.
/**
 * By default, numlock (MOD2) and keyboard layout (XKB_GROUP_INDEX) are
 * ignored. The latter is an implementation detail when using multiple
 * keyboard (layouts).
 **/
inline constexpr xpp::InputMask IGNORE_MOD{Mod::MOD2, Mod::XKB_GROUP_INDEX};

/*
 * Special keys (change & recompile nst.info accordingly)
 *
 * Mask value:
 * * Use Mod::ANY to match the key no matter modifiers state
 * * Use Mod::NONE to match the key alone (no modifiers)
 * appkeypad value: matches the current terminal's application keypad state
 * appcursor: matches the current terminal's application cursor state
 *
 * Be careful with the order of the definitions because nst searches in
 * this table sequentially, so any Mod::ANY must be in the last
 * position for a key.
 */

/// Additionally mapped keys.
/**
 * If you want keys other than the X11 function keys (0xFD00 - 0xFFFF)
 * to work, add them to this array. This set only determines
 * whether the given keys will be processed at all. Individual key
 * mappings still need to be entered below into KEYS.
 **/
inline const std::set<xpp::KeySymID> MAPPED_KEYS{};

/// List of special function key definitions.
/**
 * This is the huge list of keys which defines all compatibility to the Linux
 * world. Please decide about changes wisely.
 *
 * We use a multiset for the key definitions. The KeyID is the comparison
 * key, so we don't have to iterate over the complete list of keys linearly,
 * but only over a small list of key combinations that share the same KeyID.
 **/
inline const std::multiset<Key> KEYS{{
	// keysym               mask                              string          appkey             appcursor
	{ KeyID::KP_HOME,       Mask{Mod::SHIFT},                 "\033[2J",      AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::KP_HOME,       Mask{Mod::SHIFT},                 "\033[1;2H",    AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::KP_HOME,       Mask{Mod::ANY},                   "\033[H",       AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::KP_HOME,       Mask{Mod::ANY},                   "\033[1~",      AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::KP_UP,         Mask{Mod::ANY},                   "\033Ox",       AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_UP,         Mask{Mod::ANY},                   "\033[A",       AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::KP_UP,         Mask{Mod::ANY},                   "\033OA",       AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::KP_DOWN,       Mask{Mod::ANY},                   "\033Or",       AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_DOWN,       Mask{Mod::ANY},                   "\033[B",       AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::KP_DOWN,       Mask{Mod::ANY},                   "\033OB",       AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::KP_LEFT,       Mask{Mod::ANY},                   "\033Ot",       AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_LEFT,       Mask{Mod::ANY},                   "\033[D",       AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::KP_LEFT,       Mask{Mod::ANY},                   "\033OD",       AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::KP_RIGHT,      Mask{Mod::ANY},                   "\033Ov",       AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_RIGHT,      Mask{Mod::ANY},                   "\033[C",       AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::KP_RIGHT,      Mask{Mod::ANY},                   "\033OC",       AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::KP_PRIOR,      Mask{Mod::SHIFT},                 "\033[5;2~",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::KP_PRIOR,      Mask{Mod::ANY},                   "\033[5~",      AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::KP_BEGIN,      Mask{Mod::ANY},                   "\033[E",       AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::KP_END,        Mask{Mod::CONTROL},               "\033[J",       AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::KP_END,        Mask{Mod::CONTROL},               "\033[1;5F",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_END,        Mask{Mod::SHIFT},                 "\033[K",       AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::KP_END,        Mask{Mod::SHIFT},                 "\033[1;2F",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_END,        Mask{Mod::ANY},                   "\033[4~",      AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::KP_NEXT,       Mask{Mod::SHIFT},                 "\033[6;2~",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::KP_NEXT,       Mask{Mod::ANY},                   "\033[6~",      AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::KP_INSERT,     Mask{Mod::SHIFT},                 "\033[2;2~",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_INSERT,     Mask{Mod::SHIFT},                 "\033[4l",      AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::KP_INSERT,     Mask{Mod::CONTROL},               "\033[L",       AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::KP_INSERT,     Mask{Mod::CONTROL},               "\033[2;5~",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_INSERT,     Mask{Mod::ANY},                   "\033[4h",      AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::KP_INSERT,     Mask{Mod::ANY},                   "\033[2~",      AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_DELETE,     Mask{Mod::CONTROL},               "\033[M",       AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::KP_DELETE,     Mask{Mod::CONTROL},               "\033[3;5~",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_DELETE,     Mask{Mod::SHIFT},                 "\033[2K",      AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::KP_DELETE,     Mask{Mod::SHIFT},                 "\033[3;2~",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_DELETE,     Mask{Mod::ANY},                   "\033[P",       AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::KP_DELETE,     Mask{Mod::ANY},                   "\033[3~",      AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::KP_MULTIPLY,   Mask{Mod::ANY},                   "\033Oj",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_ADD,        Mask{Mod::ANY},                   "\033Ok",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_ENTER,      Mask{Mod::ANY},                   "\033OM",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_ENTER,      Mask{Mod::ANY},                   "\r",           AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::KP_SUBTRACT,   Mask{Mod::ANY},                   "\033Om",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_DECIMAL,    Mask{Mod::ANY},                   "\033On",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_DIVIDE,     Mask{Mod::ANY},                   "\033Oo",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_0,          Mask{Mod::ANY},                   "\033Op",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_1,          Mask{Mod::ANY},                   "\033Oq",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_2,          Mask{Mod::ANY},                   "\033Or",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_3,          Mask{Mod::ANY},                   "\033Os",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_4,          Mask{Mod::ANY},                   "\033Ot",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_5,          Mask{Mod::ANY},                   "\033Ou",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_6,          Mask{Mod::ANY},                   "\033Ov",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_7,          Mask{Mod::ANY},                   "\033Ow",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_8,          Mask{Mod::ANY},                   "\033Ox",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::KP_9,          Mask{Mod::ANY},                   "\033Oy",       AppKey::NO_NUMLOCK,AppCursor::IGNORE},
	{ KeyID::UP,            Mask{Mod::SHIFT},                 "\033[1;2A",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::UP,            Mask{Mod::MOD1},                  "\033[1;3A",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::UP,            Mask{Mod::SHIFT, Mod::MOD1},      "\033[1;4A",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::UP,            Mask{Mod::CONTROL},               "\033[1;5A",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::UP,            Mask{Mod::SHIFT, Mod::CONTROL},   "\033[1;6A",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::UP,            Mask{Mod::CONTROL, Mod::MOD1},    "\033[1;7A",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::UP,            Mask{Mod::SHIFT, Mod::CONTROL, Mod::MOD1},
		                                                  "\033[1;8A",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::UP,            Mask{Mod::ANY},                   "\033[A",       AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::UP,            Mask{Mod::ANY},                   "\033OA",       AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::DOWN,          Mask{Mod::SHIFT},                 "\033[1;2B",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::DOWN,          Mask{Mod::MOD1},                  "\033[1;3B",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::DOWN,          Mask{Mod::SHIFT, Mod::MOD1},      "\033[1;4B",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::DOWN,          Mask{Mod::CONTROL},               "\033[1;5B",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::DOWN,          Mask{Mod::SHIFT, Mod::CONTROL},   "\033[1;6B",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::DOWN,          Mask{Mod::CONTROL, Mod::MOD1},    "\033[1;7B",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::DOWN,          Mask{Mod::SHIFT, Mod::CONTROL, Mod::MOD1},
		                                                  "\033[1;8B",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::DOWN,          Mask{Mod::ANY},                   "\033[B",       AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::DOWN,          Mask{Mod::ANY},                   "\033OB",       AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::LEFT,          Mask{Mod::SHIFT},                 "\033[1;2D",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::LEFT,          Mask{Mod::MOD1},                  "\033[1;3D",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::LEFT,          Mask{Mod::SHIFT, Mod::MOD1},      "\033[1;4D",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::LEFT,          Mask{Mod::CONTROL},               "\033[1;5D",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::LEFT,          Mask{Mod::SHIFT, Mod::CONTROL},   "\033[1;6D",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::LEFT,          Mask{Mod::CONTROL,Mod::MOD1},     "\033[1;7D",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::LEFT,          Mask{Mod::SHIFT,Mod::CONTROL,Mod::MOD1},
		                                                  "\033[1;8D",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::LEFT,          Mask{Mod::ANY},                   "\033[D",       AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::LEFT,          Mask{Mod::ANY},                   "\033OD",       AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::RIGHT,         Mask{Mod::SHIFT},                 "\033[1;2C",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::RIGHT,         Mask{Mod::MOD1},                  "\033[1;3C",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::RIGHT,         Mask{Mod::SHIFT,Mod::MOD1},       "\033[1;4C",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::RIGHT,         Mask{Mod::CONTROL},               "\033[1;5C",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::RIGHT,         Mask{Mod::SHIFT,Mod::CONTROL},    "\033[1;6C",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::RIGHT,         Mask{Mod::CONTROL,Mod::MOD1},     "\033[1;7C",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::RIGHT,         Mask{Mod::SHIFT,Mod::CONTROL,Mod::MOD1},
		                                                  "\033[1;8C",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::RIGHT,         Mask{Mod::ANY},                   "\033[C",       AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::RIGHT,         Mask{Mod::ANY},                   "\033OC",       AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::ISO_LEFT_TAB,  Mask{Mod::SHIFT},                 "\033[Z",       AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::RETURN,        Mask{Mod::MOD1},                  "\033\r",       AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::RETURN,        Mask{Mod::ANY},                   "\r",           AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::INSERT,        Mask{Mod::SHIFT},                 "\033[4l",      AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::INSERT,        Mask{Mod::SHIFT},                 "\033[2;2~",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::INSERT,        Mask{Mod::CONTROL},               "\033[L",       AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::INSERT,        Mask{Mod::CONTROL},               "\033[2;5~",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::INSERT,        Mask{Mod::ANY},                   "\033[4h",      AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::INSERT,        Mask{Mod::ANY},                   "\033[2~",      AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::DELETE,        Mask{Mod::CONTROL},               "\033[M",       AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::DELETE,        Mask{Mod::CONTROL},               "\033[3;5~",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::DELETE,        Mask{Mod::SHIFT},                 "\033[2K",      AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::DELETE,        Mask{Mod::SHIFT},                 "\033[3;2~",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::DELETE,        Mask{Mod::ANY},                   "\033[P",       AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::DELETE,        Mask{Mod::ANY},                   "\033[3~",      AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::BACKSPACE,     Mask{Mod::NONE},                  "\177",         AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::BACKSPACE,     Mask{Mod::MOD1},                  "\033\177",     AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::HOME,          Mask{Mod::SHIFT},                 "\033[2J",      AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::HOME,          Mask{Mod::SHIFT},                 "\033[1;2H",    AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::HOME,          Mask{Mod::ANY},                   "\033[H",       AppKey::IGNORE,    AppCursor::DISABLED},
	{ KeyID::HOME,          Mask{Mod::ANY},                   "\033[1~",      AppKey::IGNORE,    AppCursor::ENABLED},
	{ KeyID::END,           Mask{Mod::CONTROL},               "\033[J",       AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::END,           Mask{Mod::CONTROL},               "\033[1;5F",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::END,           Mask{Mod::SHIFT},                 "\033[K",       AppKey::DISABLED,  AppCursor::IGNORE},
	{ KeyID::END,           Mask{Mod::SHIFT},                 "\033[1;2F",    AppKey::ENABLED,   AppCursor::IGNORE},
	{ KeyID::END,           Mask{Mod::ANY},                   "\033[4~",      AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::PRIOR,         Mask{Mod::CONTROL},               "\033[5;5~",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::PRIOR,         Mask{Mod::SHIFT},                 "\033[5;2~",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::PRIOR,         Mask{Mod::ANY},                   "\033[5~",      AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::NEXT,          Mask{Mod::CONTROL},               "\033[6;5~",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::NEXT,          Mask{Mod::SHIFT},                 "\033[6;2~",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::NEXT,          Mask{Mod::ANY},                   "\033[6~",      AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F1,            Mask{Mod::NONE},                  "\033OP" ,      AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F1, /* F13 */  Mask{Mod::SHIFT},                 "\033[1;2P",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F1, /* F25 */  Mask{Mod::CONTROL},               "\033[1;5P",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F1, /* F37 */  Mask{Mod::MOD4},                  "\033[1;6P",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F1, /* F49 */  Mask{Mod::MOD1},                  "\033[1;3P",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F1, /* F61 */  Mask{Mod::MOD3},                  "\033[1;4P",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F2,            Mask{Mod::NONE},                  "\033OQ" ,      AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F2, /* F14 */  Mask{Mod::SHIFT},                 "\033[1;2Q",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F2, /* F26 */  Mask{Mod::CONTROL},               "\033[1;5Q",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F2, /* F38 */  Mask{Mod::MOD4},                  "\033[1;6Q",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F2, /* F50 */  Mask{Mod::MOD1},                  "\033[1;3Q",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F2, /* F62 */  Mask{Mod::MOD3},                  "\033[1;4Q",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F3,            Mask{Mod::NONE},                  "\033OR" ,      AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F3, /* F15 */  Mask{Mod::SHIFT},                 "\033[1;2R",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F3, /* F27 */  Mask{Mod::CONTROL},               "\033[1;5R",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F3, /* F39 */  Mask{Mod::MOD4},                  "\033[1;6R",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F3, /* F51 */  Mask{Mod::MOD1},                  "\033[1;3R",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F3, /* F63 */  Mask{Mod::MOD3},                  "\033[1;4R",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F4,            Mask{Mod::NONE},                  "\033OS" ,      AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F4, /* F16 */  Mask{Mod::SHIFT},                 "\033[1;2S",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F4, /* F28 */  Mask{Mod::CONTROL},               "\033[1;5S",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F4, /* F40 */  Mask{Mod::MOD4},                  "\033[1;6S",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F4, /* F52 */  Mask{Mod::MOD1},                  "\033[1;3S",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F5,            Mask{Mod::NONE},                  "\033[15~",     AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F5, /* F17 */  Mask{Mod::SHIFT},                 "\033[15;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F5, /* F29 */  Mask{Mod::CONTROL},               "\033[15;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F5, /* F41 */  Mask{Mod::MOD4},                  "\033[15;6~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F5, /* F53 */  Mask{Mod::MOD1},                  "\033[15;3~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F6,            Mask{Mod::NONE},                  "\033[17~",     AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F6, /* F18 */  Mask{Mod::SHIFT},                 "\033[17;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F6, /* F30 */  Mask{Mod::CONTROL},               "\033[17;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F6, /* F42 */  Mask{Mod::MOD4},                  "\033[17;6~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F6, /* F54 */  Mask{Mod::MOD1},                  "\033[17;3~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F7,            Mask{Mod::NONE},                  "\033[18~",     AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F7, /* F19 */  Mask{Mod::SHIFT},                 "\033[18;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F7, /* F31 */  Mask{Mod::CONTROL},               "\033[18;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F7, /* F43 */  Mask{Mod::MOD4},                  "\033[18;6~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F7, /* F55 */  Mask{Mod::MOD1},                  "\033[18;3~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F8,            Mask{Mod::NONE},                  "\033[19~",     AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F8, /* F20 */  Mask{Mod::SHIFT},                 "\033[19;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F8, /* F32 */  Mask{Mod::CONTROL},               "\033[19;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F8, /* F44 */  Mask{Mod::MOD4},                  "\033[19;6~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F8, /* F56 */  Mask{Mod::MOD1},                  "\033[19;3~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F9,            Mask{Mod::NONE},                  "\033[20~",     AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F9, /* F21 */  Mask{Mod::SHIFT},                 "\033[20;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F9, /* F33 */  Mask{Mod::CONTROL},               "\033[20;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F9, /* F45 */  Mask{Mod::MOD4},                  "\033[20;6~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F9, /* F57 */  Mask{Mod::MOD1},                  "\033[20;3~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F10,           Mask{Mod::NONE},                  "\033[21~",     AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F10, /* F22 */ Mask{Mod::SHIFT},                 "\033[21;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F10, /* F34 */ Mask{Mod::CONTROL},               "\033[21;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F10, /* F46 */ Mask{Mod::MOD4},                  "\033[21;6~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F10, /* F58 */ Mask{Mod::MOD1},                  "\033[21;3~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F11,           Mask{Mod::NONE},                  "\033[23~",     AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F11, /* F23 */ Mask{Mod::SHIFT},                 "\033[23;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F11, /* F35 */ Mask{Mod::CONTROL},               "\033[23;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F11, /* F47 */ Mask{Mod::MOD4},                  "\033[23;6~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F11, /* F59 */ Mask{Mod::MOD1},                  "\033[23;3~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F12,           Mask{Mod::NONE},                  "\033[24~",     AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F12, /* F24 */ Mask{Mod::SHIFT},                 "\033[24;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F12, /* F36 */ Mask{Mod::CONTROL},               "\033[24;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F12, /* F48 */ Mask{Mod::MOD4},                  "\033[24;6~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F12, /* F60 */ Mask{Mod::MOD1},                  "\033[24;3~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F13,           Mask{Mod::NONE},                  "\033[1;2P",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F14,           Mask{Mod::NONE},                  "\033[1;2Q",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F15,           Mask{Mod::NONE},                  "\033[1;2R",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F16,           Mask{Mod::NONE},                  "\033[1;2S",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F17,           Mask{Mod::NONE},                  "\033[15;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F18,           Mask{Mod::NONE},                  "\033[17;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F19,           Mask{Mod::NONE},                  "\033[18;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F20,           Mask{Mod::NONE},                  "\033[19;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F21,           Mask{Mod::NONE},                  "\033[20;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F22,           Mask{Mod::NONE},                  "\033[21;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F23,           Mask{Mod::NONE},                  "\033[23;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F24,           Mask{Mod::NONE},                  "\033[24;2~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F25,           Mask{Mod::NONE},                  "\033[1;5P",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F26,           Mask{Mod::NONE},                  "\033[1;5Q",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F27,           Mask{Mod::NONE},                  "\033[1;5R",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F28,           Mask{Mod::NONE},                  "\033[1;5S",    AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F29,           Mask{Mod::NONE},                  "\033[15;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F30,           Mask{Mod::NONE},                  "\033[17;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F31,           Mask{Mod::NONE},                  "\033[18;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F32,           Mask{Mod::NONE},                  "\033[19;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F33,           Mask{Mod::NONE},                  "\033[20;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F34,           Mask{Mod::NONE},                  "\033[21;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
	{ KeyID::F35,           Mask{Mod::NONE},                  "\033[23;5~",   AppKey::IGNORE,    AppCursor::IGNORE},
}};

/// List of printable ASCII characters.
/**
 * This is used to estimate the advance width of single wide characters.
 **/
inline constexpr std::string_view ASCII_PRINTABLE{
	" !\"#$%&'()*+,-./0123456789:;<=>?"
	"@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_"
	"`abcdefghijklmnopqrstuvwxyz{|}~"
};

/// Input modifiers to influence the selection type.
/**
 * Use the same masks as usual.
 * Button1Mask is always unset, to make masks match between ButtonPress.
 * ButtonRelease and MotionNotify.
 * If no match is found, regular selection is used.
 **/
constexpr std::array<std::pair<Selection::Mode, xpp::InputMask>, 2> SEL_MASKS = {
	std::pair{Selection::Mode::RECT_RANGE, xpp::InputMask{xpp::InputModifier::CONTROL}},
	std::pair{Selection::Mode::LINE_RANGE, xpp::InputMask{xpp::InputModifier::CONTROL, xpp::InputModifier::MOD1}}
};

/// Modifier used for alternative selection behaviour.
/**
 * This modifier is currently used for two things:
 *
 * - a new selection is started and a double-click on a word delimiter with
 *   the modifier pressed occurs. Instead of regular word extension, the
 *   selection will be expanded forward until the very same word separator is
 *   encountered. Further single clicks while holding the modified will extend
 *   the selection by one field until the next very same word separator is
 *   found.
 * - a word-extended selection exists and a single-click with the modifier
 *   pressed occurs. The word selection will be further extended using
 *   WORD_DELIMITERS. If you click on the selection itself then extension is
 *   performed in both directions until another delimiter is found. If you
 *   click left/above the current selection then the selection will be
 *   extended to the left. If you click right/below the current selection
 *   then the selection will be extended to the right.
 **/
constexpr xpp::InputMask SEL_ALT_MOD{xpp::InputModifier::MOD1};

/// A list of URL schemes that will be identified as URLs and expanded in the context of word snap expansion.
/**
 * When double-clicking on such a URI scheme, then the complete URL will be
 * expanded, if possible.
 **/
inline constexpr std::string_view SEL_URI_SCHEMES[] = {"http", "https", "ftp", "git", "socks"};

// see implementation file
std::vector<MouseShortcut> get_mouse_shortcuts(Nst &nst);

// see implementation file
std::vector<KbdShortcut> get_kbd_shortcuts(Nst &nst);

} // end ns
