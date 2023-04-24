#
# spec file for package vit
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           vit
Version:        2.3.0
Release:        0
Summary:        Visual Interactive Taskwarrior full-screen terminal interface
License:        MIT
Group:          Productivity/Office/Organizers
URL:            https://github.com/scottkosty/vit
Source:         https://files.pythonhosted.org/packages/source/v/vit/vit-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base >= 3.7
BuildRequires:  python3-setuptools
BuildRequires:  python3-tasklib
BuildRequires:  python3-urwid
Requires:       python3-base >= 3.7
Requires:       python3-tasklib
Requires:       python3-urwid
Requires:       taskwarrior
BuildArch:      noarch

%description
Visual Interactive Taskwarrior full-screen terminal interface.
Features:
 * Fully-customizable key bindings (default Vim-like)
 * Uncluttered display
 * No mouse
 * Speed
 * Per-column colorization
 * Advanced tab completion
 * Multiple/customizable themes
 * Override/customize column formatters
 * Intelligent sub-project indenting

%prep
%setup -q -n vit-%{version}

%build
%python3_build

%install
%python3_install
install -Dm644 scripts/bash/vit.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/vit
%fdupes %{buildroot}%{python3_sitelib}

%check
python3 -m unittest

%files
%doc COLOR.md CUSTOMIZE.md README.md
%license LICENSE
%{_bindir}/vit
%{_datadir}/bash-completion/completions/vit
%{python3_sitelib}/*

%changelog
