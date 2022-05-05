-- mod-version:2
local core = require "core"
local config = require "core.config"
local DocView = require "core.docview"
local Doc = require "core.doc"
local common = require "core.common"
local command = require "core.command"
local style = require "core.style"
local gitdiff = require "plugins.gitdiff_highlight.gitdiff"
local _, MiniMap = pcall(require, "plugins.minimap")

-- vscode defaults
style.gitdiff_addition = {common.color "#587c0c"}
style.gitdiff_modification = {common.color "#0c7d9d"}
style.gitdiff_deletion = {common.color "#94151b"}

local function color_for_diff(diff)
	if diff == "addition" then
		return style.gitdiff_addition
	elseif diff == "modification" then
		return style.gitdiff_modification
	else
		return style.gitdiff_deletion
	end
end

style.gitdiff_width = 3

local last_doc_lines = 0

-- maximum size of git diff to read, multiplied by current filesize
config.max_diff_size = 2


local diffs = setmetatable({}, { __mode = "k" })

local function get_diff(doc)
	return diffs[doc] or {is_in_repo = false}
end

local function init_diff(doc)
	diffs[doc] = {is_in_repo = true}
end

local function update_diff(doc)
	if doc == nil or doc.filename == nil then return end

	local current_file
	if system.get_file_info(doc.filename) then
		current_file = system.absolute_path(doc.filename)
	else
		current_file = doc.filename
	end

	core.log_quiet("updating diff for " .. current_file)

	if not get_diff(doc).is_in_repo then
		local is_in_repo = process.start({"git", "ls-files", "--error-unmatch", current_file})
		while is_in_repo:running() do
		  coroutine.yield(0.1)
		end
		is_in_repo = is_in_repo:returncode()
		is_in_repo = is_in_repo == 0
		if is_in_repo then
			init_diff(doc)
		else
			core.log_quiet("file ".. current_file .." is not in a git repository")
			return
		end
	end

	local max_diff_size = system.get_file_info(current_file).size * config.max_diff_size
	local diff_proc = process.start({"git", "diff", "HEAD", "--word-diff", "--unified=1", "--no-color", current_file})
	while diff_proc:running() do
		coroutine.yield(0.1)
	end
	local raw_diff = diff_proc:read_stdout(max_diff_size)
	local parsed_diff = gitdiff.changed_lines(raw_diff)
	diffs[doc] = parsed_diff
	diffs[doc].is_in_repo = true
end


local function gitdiff_padding(dv)
	return style.padding.x * 1.5 + dv:get_font():get_width(#dv.doc.lines)
end

local old_docview_gutter = DocView.draw_line_gutter
local old_gutter_width = DocView.get_gutter_width
function DocView:draw_line_gutter(idx, x, y, width)
	if not get_diff(self.doc).is_in_repo then
		return old_docview_gutter(self, idx, x, y, width)
	end

	local gw, gpad = old_gutter_width(self)

	old_docview_gutter(self, idx, x, y, gpad and gw - gpad or gw)

	if diffs[self.doc][idx] == nil then
		return
	end

	local color = color_for_diff(diffs[self.doc][idx])

	-- add margin in between highlight and text
	x = x + gitdiff_padding(self)
	local yoffset = self:get_line_text_y_offset()
	if diffs[self.doc][idx] ~= "deletion" then
		renderer.draw_rect(x, y + yoffset, style.gitdiff_width, self:get_line_height(), color)
		return
	end
	renderer.draw_rect(x, y + (yoffset * 4), style.gitdiff_width, self:get_line_height() / 2, color)
end

function DocView:get_gutter_width()
	if not get_diff(self.doc).is_in_repo then return old_gutter_width(self) end
	return old_gutter_width(self) + style.padding.x * style.gitdiff_width / 12
end

local old_text_change = Doc.on_text_change
function Doc:on_text_change(type)
	local line
	if not get_diff(self).is_in_repo then goto end_of_function end
	line = self:get_selection()
	if diffs[self][line] == "addition" then goto end_of_function end
	-- TODO figure out how to detect an addition
	if type == "insert" or (type == "remove" and #self.lines == last_doc_lines) then
		diffs[self][line] = "modification"
	elseif type == "remove" then
		diffs[self][line] = "deletion"
	end
	::end_of_function::
	last_doc_lines = #self.lines
	return old_text_change(self, type)
end


local old_doc_save = Doc.save
function Doc:save(...)
	old_doc_save(self, ...)
	core.add_thread(function()
		update_diff(self)
	end)
end

local old_docview_new = DocView.new
function DocView:new(...)
	old_docview_new(self, ...)
	core.add_thread(function()
		update_diff(self.doc)
	end)
end

local old_doc_load = Doc.load
function Doc:load(...)
	old_doc_load(self, ...)
	core.add_thread(function()
		update_diff(self)
	end)
end

if type(MiniMap) == "table" then
	-- Override MiniMap's line_highlight_color, but first
	-- stash the old one (using [] in case it is not there at all)
	local old_line_highlight_color = MiniMap["line_highlight_color"]
	function MiniMap:line_highlight_color(line_index)
		local diff = get_diff(core.active_view.doc)
		if diff.is_in_repo and diff[line_index] then
			return color_for_diff(diff[line_index])
		end
		return old_line_highlight_color(line_index)
	end
end

local function jump_to_next_change()
	local doc = core.active_view.doc
	local line, col = doc:get_selection()
	if not get_diff(doc).is_in_repo then return end

	while diffs[doc][line] do
		line = line + 1
	end

	while line < #doc.lines do
		if diffs[doc][line] then
			doc:set_selection(line, col, line, col)
			return
		end
		line = line + 1
	end
end

local function jump_to_previous_change()
	local doc = core.active_view.doc
	local line, col = doc:get_selection()
	if not get_diff(doc).is_in_repo then return end

	while diffs[doc][line] do
		line = line - 1
	end

	while line > 0 do
		if diffs[doc][line] then
			doc:set_selection(line, col, line, col)
			return
		end
		line = line - 1
	end
end

command.add("core.docview", {
	["gitdiff:previous-change"] = function()
		jump_to_previous_change()
	end,

	["gitdiff:next-change"] = function()
		jump_to_next_change()
	end,
})

