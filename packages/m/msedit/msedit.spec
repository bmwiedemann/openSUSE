#
# spec file for package msedit
#
# Copyright (c) 2025 SUSE LLC
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


Name:           msedit
Summary:        A simple editor for simple needs
URL:            https://github.com/microsoft/edit
Version:        1.2.0
Release:        0
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
License:        MIT
BuildRequires:  cargo >= 1.84
BuildRequires:  cargo-packaging
BuildRequires:  libicu-devel
BuildRequires:  libzstd-devel
BuildRequires:  update-desktop-files

%description
This editor pays homage to the classic MS-DOS Editor, but with a modern
interface and input controls similar to VS Code. The goal is to provide
an accessible editor that even users largely unfamiliar with terminals can
easily use.

%prep
%autosetup -a1

%build
export RUSTC_BOOTSTRAP=1
%{cargo_build}

%check
export RUSTC_BOOTSTRAP=1
%{cargo_test}

%install
export RUSTC_BOOTSTRAP=1
%{cargo_install}
mv %{buildroot}%{_bindir}/edit %{buildroot}%{_bindir}/msedit
install -Dm644 -T %{_builddir}/%{buildsubdir}/assets/manpage/edit.1 %{buildroot}%{_mandir}/man1/%{name}.1

install -Dm644 -T %{_builddir}/%{buildsubdir}/assets/com.microsoft.edit.desktop \
	%{buildroot}%{_datadir}/applications/com.microsoft.edit.desktop
%suse_update_desktop_file com.microsoft.edit
sed -i "6s/edit/%{name}/g" %{buildroot}%{_datadir}/applications/com.microsoft.edit.desktop
sed -i "7s/edit/%{name}/g" %{buildroot}%{_datadir}/applications/com.microsoft.edit.desktop
install -Dm644 -T %{_builddir}/%{buildsubdir}/assets/edit.svg \
	%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files
%defattr(-,root,root,-)
%{_bindir}/msedit
%doc *.md
%dir %{_datadir}/icons
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/com.microsoft.edit.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}
%license LICENSE

%changelog
