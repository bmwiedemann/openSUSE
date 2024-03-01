// C++
#include <functional>

// nst
#include "nst.hxx"
#include "WindowSystem.hxx"

/*
 * the implementation of these are placed in this separate file since they
 * need data structures that would cause circular dependencies when included
 * in the config header
 */

namespace nst::config {

static_assert(COLS > 1);
static_assert(ROWS > 1);

/// Internal mouse shortcuts.
/**
 * Beware that overloading Button1 will disable the selection behaviour.
 **/
std::vector<MouseShortcut> get_mouse_shortcuts(Nst &nst) {

	auto &tty = nst.tty();
	auto &wsys = nst.wsys();
	auto &term = nst.term();

	auto ttysend = [&](const std::string_view s) {
		tty.write(s, TTY::MayEcho{true});
	};

	using xpp::Button;

	auto scrollHistoryUp = [&term, ttysend](bool shift) {
		// on the alt screen we inject special escape sequences that
		// are used by programs like less and vim for scrolling.
		if (term.onAltScreen()) {
			ttysend("\031");
		} else {
			if (shift)
				term.scrollHistoryUpByPage(0.5);
			else
				term.scrollHistoryUpByLines(+5);
		}
	};

	auto scrollHistoryDown = [&term, ttysend](bool shift) {
		// see above
		if (term.onAltScreen()) {
			ttysend("\005");
		} else {
			if (shift)
				term.scrollHistoryDownByPage(0.5);
			else
				term.scrollHistoryDownByLines(+5);
		}
	};

	return {
		//             mask              button           function                                         release
		MouseShortcut{ Mask{Mod::ANY},   Button::BUTTON2, std::bind(&WindowSystem::pasteSelection, &wsys), true,   StopScrolling{true}},
		// change font size similar to how it works in web browsers
		MouseShortcut{ Mask{Mod::CONTROL}, Button::BUTTON4, std::bind(&WindowSystem::zoomFont, &wsys, +1), false },
		MouseShortcut{ Mask{Mod::CONTROL}, Button::BUTTON5, std::bind(&WindowSystem::zoomFont, &wsys, -1), false },
		// these generate sequences used by less/vi for scrolling
		MouseShortcut{ Mask{Mod::SHIFT}, Button::BUTTON4, std::bind(scrollHistoryUp, true),                false },
		MouseShortcut{ Mask{Mod::SHIFT}, Button::BUTTON5, std::bind(scrollHistoryDown, true),              false },
		// regular scrolling via mouse wheel
		MouseShortcut{ Mask{Mod::ANY},   Button::BUTTON4, std::bind(scrollHistoryUp, false),               false },
		MouseShortcut{ Mask{Mod::ANY},   Button::BUTTON5, std::bind(scrollHistoryDown, false),             false },
	};
}

/// Internal keyboard shortcuts.
std::vector<KbdShortcut> get_kbd_shortcuts(Nst &nst) {
	//constexpr auto MODKEY = Mod1Mask;
	constexpr xpp::InputMask TERMMOD{Mod::CONTROL, Mod::SHIFT};

	auto &tty = nst.tty();
	auto &wsys = nst.wsys();
	auto &term = nst.term();
	auto selPaste = std::bind(&WindowSystem::pasteSelection, &wsys);

	auto togglePrinter = [&]() { term.setPrintMode(!term.isPrintMode()); };
	auto printScreen   = [&]() { term.dump(); };
	auto printSel      = [&]() { nst.selection().dump(); };

	return {
		// mask                 keysym              function
		{ Mask{Mod::ANY},       KeyID::BREAK,       std::bind(&TTY::sendBreak, &tty) },
		{ Mask{Mod::CONTROL},   KeyID::PRINT,       togglePrinter       },
		{ Mask{Mod::SHIFT},     KeyID::PRINT,       printScreen         },
		{ Mask{Mod::ANY},       KeyID::PRINT,       printSel            },
		{ Mask{Mod::SHIFT,
		      Mod::MOD1},       KeyID::PRIOR,       std::bind(&WindowSystem::zoomFont, &wsys, +1) },
		{ Mask{Mod::SHIFT,
		      Mod::MOD1},       KeyID::NEXT,        std::bind(&WindowSystem::zoomFont, &wsys, -1) },
		{ Mask{Mod::SHIFT,
		      Mod::MOD1},       KeyID::HOME,        std::bind(&WindowSystem::resetFont, &wsys) },
		{ TERMMOD,              KeyID::C,           std::bind(&WindowSystem::copyToClipboard, &wsys) },
		{ TERMMOD,              KeyID::V,           std::bind(&WindowSystem::pasteClipboard, &wsys), StopScrolling{true} },
		{ TERMMOD,              KeyID::Y,           selPaste, StopScrolling{true}            },
		{ Mask{Mod::SHIFT},     KeyID::INSERT,      selPaste, StopScrolling{true}            },
		{ TERMMOD,              KeyID::NUM_LOCK,    std::bind(&WindowSystem::toggleNumlock, &wsys) },
		{ Mask{Mod::SHIFT},     KeyID::PRIOR,       std::bind(&nst::Term::scrollHistoryUpByLines, &term, +10) },
		{ Mask{Mod::SHIFT},     KeyID::NEXT,        std::bind(&nst::Term::scrollHistoryDownByLines, &term, +10) },
		{ TERMMOD,              KeyID::PRIOR,       std::bind(&nst::Term::scrollHistoryUpByPage, &term, +0.5) },
		{ TERMMOD,              KeyID::NEXT,        std::bind(&nst::Term::scrollHistoryDownByPage, &term, +0.5) },
		{ TERMMOD,              KeyID::HOME,        std::bind(&nst::Term::scrollHistoryUpMax, &term) },
		{ TERMMOD,              KeyID::END,         std::bind(&nst::Term::stopScrolling, &term) },
		{ TERMMOD,              KeyID::B,           std::bind(&nst::Nst::pipeBufferTo, &nst, cosmos::StringViewVector{"gvim", "--not-a-term", "-"}) },
		{ Mask{},               KeyID::F11,         std::bind(&WindowSystem::toggleFullScreen, &wsys) },
		{ TERMMOD,              KeyID::KP_DIVIDE,   std::bind(&WindowSystem::invertColors, &wsys) }
	};
}

} // ns nst::config
