-- OKARU: generado desde la paleta activa. Se usa con :colorscheme okaru
vim.cmd("highlight clear")
if vim.g.syntax_on then vim.cmd("syntax reset") end
vim.o.background = "{{ mode }}"
vim.o.termguicolors = true
vim.g.colors_name = "okaru"

local c = {
  bg = "{{ colors.surface.default.hex }}",
  bg_low = "{{ colors.surface_container_low.default.hex }}",
  bg_mid = "{{ colors.surface_container.default.hex }}",
  bg_high = "{{ colors.surface_container_high.default.hex }}",
  bg_top = "{{ colors.surface_container_highest.default.hex }}",
  fg = "{{ colors.on_surface.default.hex }}",
  fg_dim = "{{ colors.on_surface_variant.default.hex }}",
  outline = "{{ colors.outline.default.hex }}",
  line = "{{ colors.outline_variant.default.hex }}",
  primary = "{{ colors.primary.default.hex }}",
  on_primary = "{{ colors.on_primary.default.hex }}",
  primary_box = "{{ colors.primary_container.default.hex }}",
  on_primary_box = "{{ colors.on_primary_container.default.hex }}",
  secondary = "{{ colors.secondary.default.hex }}",
  secondary_box = "{{ colors.secondary_container.default.hex }}",
  on_secondary_box = "{{ colors.on_secondary_container.default.hex }}",
  tertiary = "{{ colors.tertiary.default.hex }}",
  tertiary_box = "{{ colors.tertiary_container.default.hex }}",
  on_tertiary_box = "{{ colors.on_tertiary_container.default.hex }}",
  error = "{{ colors.error.default.hex }}",
  error_box = "{{ colors.error_container.default.hex }}",
  ok = "{{ colors.added.default.hex }}",
  ok_box = "{{ colors.added_container.default.hex }}",
  warn = "{{ colors.caution.default.hex }}",
  warn_box = "{{ colors.caution_container.default.hex }}",
}

local groups = {
  Normal = { fg = c.fg, bg = c.bg }, NormalNC = { fg = c.fg, bg = c.bg },
  NormalFloat = { fg = c.fg, bg = c.bg_high }, FloatBorder = { fg = c.line, bg = c.bg_high },
  FloatTitle = { fg = c.primary, bg = c.bg_high, bold = true },
  Cursor = { fg = c.bg, bg = c.primary }, CursorLine = { bg = c.bg_low }, CursorColumn = { bg = c.bg_low },
  ColorColumn = { bg = c.bg_low }, LineNr = { fg = c.outline }, CursorLineNr = { fg = c.primary, bold = true },
  SignColumn = { bg = c.bg }, FoldColumn = { fg = c.outline }, Folded = { fg = c.fg_dim, bg = c.bg_mid },
  VertSplit = { fg = c.line }, WinSeparator = { fg = c.line }, EndOfBuffer = { fg = c.bg },
  NonText = { fg = c.line }, Whitespace = { fg = c.line }, SpecialKey = { fg = c.line },
  Visual = { bg = c.primary_box }, VisualNOS = { bg = c.primary_box },
  Search = { fg = c.on_tertiary_box, bg = c.tertiary_box }, IncSearch = { fg = c.on_primary, bg = c.primary },
  CurSearch = { fg = c.on_primary, bg = c.primary }, Substitute = { fg = c.on_primary, bg = c.error },
  MatchParen = { fg = c.primary, bold = true, underline = true },
  Pmenu = { fg = c.fg, bg = c.bg_high }, PmenuSel = { fg = c.on_secondary_box, bg = c.secondary_box },
  PmenuSbar = { bg = c.bg_high }, PmenuThumb = { bg = c.outline },
  StatusLine = { fg = c.fg, bg = c.bg_high }, StatusLineNC = { fg = c.outline, bg = c.bg_mid },
  TabLine = { fg = c.fg_dim, bg = c.bg_mid }, TabLineSel = { fg = c.on_primary, bg = c.primary, bold = true },
  TabLineFill = { bg = c.bg_mid }, WinBar = { fg = c.fg_dim }, WinBarNC = { fg = c.outline },
  Title = { fg = c.primary, bold = true }, Directory = { fg = c.primary },
  ErrorMsg = { fg = c.error, bold = true }, WarningMsg = { fg = c.warn }, MoreMsg = { fg = c.ok },
  ModeMsg = { fg = c.fg_dim }, Question = { fg = c.secondary }, QuickFixLine = { bg = c.secondary_box },
  SpellBad = { sp = c.error, undercurl = true }, SpellCap = { sp = c.warn, undercurl = true },
  SpellLocal = { sp = c.secondary, undercurl = true }, SpellRare = { sp = c.tertiary, undercurl = true },
  DiffAdd = { bg = c.ok_box }, DiffChange = { bg = c.warn_box }, DiffDelete = { fg = c.error, bg = c.error_box },
  DiffText = { fg = c.fg, bg = c.warn_box, bold = true },
  Added = { fg = c.ok }, Changed = { fg = c.warn }, Removed = { fg = c.error },

  Comment = { fg = c.outline, italic = true }, Constant = { fg = c.tertiary }, String = { fg = c.ok },
  Character = { fg = c.ok }, Number = { fg = c.tertiary }, Boolean = { fg = c.tertiary }, Float = { fg = c.tertiary },
  Identifier = { fg = c.fg }, Function = { fg = c.primary }, Statement = { fg = c.secondary, bold = true },
  Keyword = { fg = c.secondary, bold = true }, Conditional = { fg = c.secondary }, Repeat = { fg = c.secondary },
  Label = { fg = c.secondary }, Operator = { fg = c.fg_dim }, Exception = { fg = c.error },
  PreProc = { fg = c.warn }, Include = { fg = c.secondary }, Define = { fg = c.warn }, Macro = { fg = c.warn },
  Type = { fg = c.tertiary }, StorageClass = { fg = c.secondary }, Structure = { fg = c.tertiary },
  Typedef = { fg = c.tertiary }, Special = { fg = c.primary }, SpecialChar = { fg = c.warn },
  Delimiter = { fg = c.fg_dim }, Tag = { fg = c.primary }, Underlined = { fg = c.primary, underline = true },
  Error = { fg = c.error }, Todo = { fg = c.bg, bg = c.warn, bold = true },

  DiagnosticError = { fg = c.error }, DiagnosticWarn = { fg = c.warn },
  DiagnosticInfo = { fg = c.primary }, DiagnosticHint = { fg = c.secondary }, DiagnosticOk = { fg = c.ok },
  DiagnosticUnderlineError = { sp = c.error, undercurl = true },
  DiagnosticUnderlineWarn = { sp = c.warn, undercurl = true },
  DiagnosticUnderlineInfo = { sp = c.primary, undercurl = true },
  DiagnosticUnderlineHint = { sp = c.secondary, undercurl = true },
  DiagnosticVirtualTextError = { fg = c.error, bg = c.error_box },
  DiagnosticVirtualTextWarn = { fg = c.warn, bg = c.warn_box },
  LspReferenceText = { bg = c.bg_high }, LspReferenceRead = { bg = c.bg_high },
  LspReferenceWrite = { bg = c.bg_top }, LspInlayHint = { fg = c.outline, italic = true },

  ["@variable"] = { fg = c.fg }, ["@variable.builtin"] = { fg = c.secondary, italic = true },
  ["@variable.parameter"] = { fg = c.fg, italic = true }, ["@variable.member"] = { fg = c.fg },
  ["@property"] = { fg = c.fg }, ["@function"] = { link = "Function" }, ["@function.builtin"] = { fg = c.primary },
  ["@function.method"] = { link = "Function" }, ["@constructor"] = { fg = c.primary },
  ["@keyword"] = { link = "Keyword" }, ["@keyword.return"] = { fg = c.secondary, bold = true },
  ["@type"] = { link = "Type" }, ["@type.builtin"] = { fg = c.tertiary, italic = true },
  ["@string"] = { link = "String" }, ["@string.escape"] = { fg = c.warn }, ["@string.regexp"] = { fg = c.warn },
  ["@number"] = { link = "Number" }, ["@boolean"] = { link = "Boolean" }, ["@constant"] = { link = "Constant" },
  ["@constant.builtin"] = { fg = c.tertiary, italic = true }, ["@module"] = { fg = c.tertiary },
  ["@punctuation"] = { fg = c.fg_dim }, ["@punctuation.bracket"] = { fg = c.fg_dim },
  ["@tag"] = { fg = c.primary }, ["@tag.attribute"] = { fg = c.tertiary }, ["@tag.delimiter"] = { fg = c.fg_dim },
  ["@comment"] = { link = "Comment" }, ["@markup.heading"] = { fg = c.primary, bold = true },
  ["@markup.link"] = { fg = c.primary, underline = true }, ["@markup.raw"] = { fg = c.ok },
  ["@markup.strong"] = { bold = true }, ["@markup.italic"] = { italic = true },
  ["@diff.plus"] = { fg = c.ok }, ["@diff.minus"] = { fg = c.error }, ["@diff.delta"] = { fg = c.warn },

  GitSignsAdd = { fg = c.ok }, GitSignsChange = { fg = c.warn }, GitSignsDelete = { fg = c.error },
}
for name, spec in pairs(groups) do
  vim.api.nvim_set_hl(0, name, spec)
end

local term = {
  "{{ colors.terminal_normal_black.default.hex }}", "{{ colors.terminal_normal_red.default.hex }}",
  "{{ colors.terminal_normal_green.default.hex }}", "{{ colors.terminal_normal_yellow.default.hex }}",
  "{{ colors.terminal_normal_blue.default.hex }}", "{{ colors.terminal_normal_magenta.default.hex }}",
  "{{ colors.terminal_normal_cyan.default.hex }}", "{{ colors.terminal_normal_white.default.hex }}",
  "{{ colors.terminal_bright_black.default.hex }}", "{{ colors.terminal_bright_red.default.hex }}",
  "{{ colors.terminal_bright_green.default.hex }}", "{{ colors.terminal_bright_yellow.default.hex }}",
  "{{ colors.terminal_bright_blue.default.hex }}", "{{ colors.terminal_bright_magenta.default.hex }}",
  "{{ colors.terminal_bright_cyan.default.hex }}", "{{ colors.terminal_bright_white.default.hex }}",
}
for i, color in ipairs(term) do
  vim.g["terminal_color_" .. (i - 1)] = color
end
