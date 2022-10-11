#
# spec file for package mac
#
# Copyright (c) 2022 SUSE LLC
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


%define _version 892
Name:           mac
Version:        8.92
Release:        0
Summary:        APE codec and decompressor
License:        SUSE-Permissive
URL:            https://www.monkeysaudio.com/index.html
Source0:        https://monkeysaudio.com/files/MAC_%{_version}_SDK.zip
Source1:        https://monkeysaudio.com/license.html
BuildRequires:  gcc-c++
BuildRequires:  unzip
BuildRequires:  %{python_module html2text}
%debug_package

%description
Monkey’s Audio is a fast and easy way to compress digital music.

%postun
ldconfig

%post
ldconfig

%package devel
Summary:        Development files for APE
Requires:       mac = %{version}
BuildArch:      noarch

%description devel
Development files for Monkey's Audio codec and decompressor.

%prep
%setup -qc
tr -d '\r' <Readme.txt >README
ls -l
html2text --ignore-links "%{_sourcedir}/license.html" | sed -n '/^## License$/,$p' > LICENSE.md

%build
%make_build -C Source/Projects/NonWindows

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} install -C Source/Projects/NonWindows
install -d %{buildroot}%{_docdir}
install -m0644 LICENSE.md %{buildroot}%{_docdir}

%files
%doc README
%license %{_docdir}/LICENSE.md
%{_bindir}/mac
%{_prefix}/lib/libMAC.so.8

%files devel
%{_includedir}/*
%{_prefix}/lib/libMAC.so

%changelog
