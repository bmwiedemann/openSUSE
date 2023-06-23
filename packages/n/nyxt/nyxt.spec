#
# spec file for package nyxt
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


# WebExtension support is not included by default because it's unfinished
# and possibly prone to security issues. 
%bcond_with webextensions

Name:           nyxt
Version:        3.2.1
Release:        0
Summary:        Keyboard-oriented, Common Lisp extensible web-browser
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Browsers
URL:            https://nyxt.atlas.engineer
Source:         nyxt-%{version}-source-with-submodules.tar.xz
Patch0:         so_ver_fix.patch
Requires:       libwebkit2gtk-4_1-0
Requires:       libfixposix4
Requires:       enchant-tools
Requires:       glib-networking
Requires:       gsettings-desktop-schemas
Requires:       xclip
BuildRequires:  pkgconfig(libfixposix)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
Buildrequires:  pkgconfig(libcrypto)
BuildRequires:  sbcl
BuildRequires:  gcc-c++
BuildRequires:  git
Conflicts:      nyxt-git

%description
Nyxt is a keyboard-oriented, extensible web-browser designed for power users. It has familiar key-bindings (Emacs, VI, CUA), is fully configurable and extensible in Lisp, and has powerful features for productive professionals.

%prep
%setup -q -c nyxt-%{version}
%patch0 -p1

%build

%if %{with webextensions}
make all web-extensions PREFIX=/usr LIBDIR=%{_libdir} NASDF_COMPRESS=T
%else
make all PREFIX=/usr LIBDIR=%{_libdir} NASDF_COMPRESS=T
%endif


%install

%make_install PREFIX=/usr LIBDIR=%{buildroot}/%{_libdir}

%if %{with webextensions}
strip -s %{buildroot}/%{_libdir}/nyxt/libnyxt.so
%endif

%files
%{_bindir}/nyxt
%if %{with webextensions}
%{_libdir}/nyxt/
%endif
%{_datadir}/nyxt/
%{_datadir}/icons/hicolor/*/apps/nyxt.png
%{_datadir}/applications/nyxt.desktop
%doc README.org
%license licenses/ASSET-LICENSE
%license licenses/SOURCE-LICENSE

%changelog
