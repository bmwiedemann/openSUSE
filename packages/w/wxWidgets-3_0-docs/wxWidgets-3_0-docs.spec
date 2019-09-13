#
# spec file for package wxWidgets-3_0-docs
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           wxWidgets-3_0-docs
Version:        3.0.4
Release:        0
Url:            http://wxwidgets.org/
Summary:        wxWidgets Documentation
License:        GPL-2.0+
Group:          Documentation/HTML

Source:         https://github.com/wxWidgets/wxWidgets/releases/download/v%{version}/wxWidgets-%{version}-docs-html.tar.bz2
Source2:        wxWidgets-3_0-docs-rpmlintrc
BuildRequires:  fdupes
Provides:       wxWidgets-docs = %version-%release
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains wxWidgets documentation in HTML format.

%prep
%setup -qn wxWidgets-%version-docs-html

%build

%install
mkdir -p %buildroot/%_docdir/wxWidgets-3_0
cp -r . %buildroot/%_docdir/wxWidgets-3_0
%fdupes %buildroot/%_prefix

%files
%defattr(-,root,root)
%doc %_docdir/wxWidgets-3_0/

%changelog
