#
# spec file for package gap-alco
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gap-typeset
Version:        1.2.3
Release:        0
Summary:        GAP: Automatic typesetting framework for common GAP objects
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/typeset/
#Git-Clone:     https://github.com/gap-packages/typeset
Source:         https://github.com/gap-packages/typeset/releases/download/v%version/typeset-%version.tar.gz
BuildArch:      noarch
BuildRequires:  gap-rpm-devel
Requires:       gap-core >= 4.11
Suggests:       gap-digraphs >= 1.5.0

%description
This GAP package implements a framework for automatic typesetting of
common GAP objects, for the purpose of embedding them nicely into
research papers. Currently, an example implementation has been
written specifically for LaTeX.

%prep
%autosetup -n typeset-%version

%build

%install
%gappkg_simple_install

%files -f %name.files

%changelog
