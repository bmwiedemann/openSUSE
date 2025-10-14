#
# spec file for package decker-doc
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


Name:           decker-doc
Version:        1.60
Release:        0
Summary:        A multimedia sketchpad
License:        MIT
URL:            http://beyondloom.com/decker/
Source:         https://github.com/JohnEarnest/Decker/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  decker
BuildArch:      noarch

%description
Decker is a multimedia platform for creating and sharing interactive documents, with sound, images, hypertext, and scripted behavior.

%prep
%autosetup -p1 -n Decker-%{version}

%build
lilt scripts/lildoc.lil docs/lil.md         docs/lil.html
lilt scripts/lildoc.lil docs/lilt.md        docs/lilt.html
lilt scripts/lildoc.lil docs/decker.md      docs/decker.html
lilt scripts/lildoc.lil docs/format.md      docs/format.html
lilt scripts/lildoc.lil docs/lilquickref.md docs/lilquickref.html

%install
mkdir -p %{buildroot}/%{_docdir}/decker
install --mode=644 docs/*.html %{buildroot}/%{_docdir}/decker
install -d examples/ %{buildroot}/%{_docdir}/decker

%files
%license LICENSE.txt
%doc Readme.md VERSION
%{_docdir}/decker

%changelog
