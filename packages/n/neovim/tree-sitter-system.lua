-- Universal loader for system Tree-sitter parsers with automatic filetype mapping
-- Includes ABI check with detailed warning to :messages
-- Self-contained: only depends on Neovim built-ins

local FILETYPE_OVERRIDES = {
  vimdoc = 'vim',
  tsx = 'typescript.tsx',
  jinja2 = 'jinja',
  wikitext = 'mediawiki',
}

-- Parsers whose exported C symbol does not match the underscore-converted
-- language name (i.e. tree_sitter_<value> instead of tree_sitter_<lang>).
local SYMBOL_OVERRIDES = {
  go_sum = 'gosum',
  gpg_config = 'gpg',
}

local uv = vim.uv

-- On multilib systems both /usr/lib and /usr/lib64 may exist;
-- pick the longest match (i.e. the native 64-bit libdir).
local parser_dirs = vim.fn.glob('/usr/lib*/tree-sitter', false, true)
table.sort(parser_dirs, function(a, b) return #a > #b end)
local parser_dir = parser_dirs[1]

-- Helper: convert filename to Neovim-safe language name
---@param fname string # The filename (e.g., 'libtree-sitter-lua.so')
---@return string? # Returns the sanitized language name or nil if no match
local function sanitize_langname(fname)
  -- Strip the 'libtree-sitter-' prefix and '.so' suffix
  local name = fname:match('^libtree%-sitter%-(.+)%.so$')
  if not name then
    -- Fallback: just strip .so (for unexpected naming schemes)
    name = fname:match('(.+)%.so$')
  end
  if name then
    ---@cast name string
    name = name:gsub('-', '_')
    return name
  else
    vim.notify(
      string.format('Failed to sanitize filename: %s', fname),
      vim.log.levels.DEBUG
    )
    return nil
  end
end

-- Helper: guess filetype from parser name
---@param lang string
---@return string
local function guess_filetype(lang)
  local ft = lang:gsub('_inline$', ''):gsub('_sum$', ''):gsub('%d+$', '')
  return FILETYPE_OVERRIDES[ft] or ft
end

-- Iterate over all .so files in parser_dir
if not parser_dir then
  vim.notify(
    'No tree-sitter parser directory found matching /usr/lib*/tree-sitter',
    vim.log.levels.DEBUG
  )
  return
end

local handle = uv.fs_scandir(parser_dir)
if not handle then
  vim.notify(
    string.format('Tree-sitter parser directory not readable: %s', parser_dir),
    vim.log.levels.DEBUG
  )
  return
end

while true do
  local filename = uv.fs_scandir_next(handle)
  if not filename then
    break
  end

  if filename:match('%.so$') then
    local lang = sanitize_langname(filename)
    if lang then
      local parser_path = parser_dir .. '/' .. filename
      local symbol_name = SYMBOL_OVERRIDES[lang]
      local ok, result = pcall(vim.treesitter.language.add, lang, {
        path = parser_path,
        symbol_name = symbol_name,
      })

      if ok and result then
        local ft = guess_filetype(lang)
        vim.treesitter.language.register(lang, ft)
      else
        local err = ok and 'unknown error' or tostring(result)
        vim.schedule(function()
          vim.notify(
            string.format(
              "Tree-sitter parser '%s' (%s) failed to load: %s",
              lang,
              parser_path,
              err
            ),
            vim.log.levels.WARN
          )
        end)
      end
    end
  end
end
