#
# spec file for package c-intro-and-ref
#
# Copyright (c) 2025 Björn Bidar
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


Name:           c-intro-and-ref
Summary:        GNU C Language Intro and Reference
Version:        20240831.93.6296201
Release:        0
License:        GFDL-1.3-or-later
Group:          Documentation/Other
URL:            https://www.gnu.org
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
# Info variant
BuildRequires:  makeinfo
# Pdf
BuildRequires:  texinfo
BuildArch:      noarch

%global _description This manual explains the C language for use with the GNU Compiler Collection (GCC) \
on the GNU/Linux system and other systems. We refer to this dialect as GNU C.\
If you already know C, you can use this as a reference manual.

%description
%{_description}

%package info
Summary:        %{summary} - info version

%description info
%{_description}

This package provides the documentation in the Info format.

%package html
Summary:        %{summary} - HTML version

%description html
%{_description}

This package provides the documentation in the HTML format.

%package pdf
Summary:        %{summary} - PDF version

%description pdf

%{_description}

This package provides the documentation in the PDF format.

%prep
%autosetup -p1

%build
autoreconf \
    --install \
    --symlink
%configure \
    --docdir=%{_docdir}

%make_build all html  AM_MAKEINFOHTMLFLAG=--no-split

%install
%make_install install install-html

%files pdf
%doc %{_docdir}/c.pdf

%files html
%doc %{_docdir}/c.html

%files info
%doc %{_infodir}/c.info%{ext_info}
%doc %{_infodir}/c.info-1%{ext_info}
%doc %{_infodir}/c.info-2%{ext_info}
%doc %{_infodir}/c.info-3%{ext_info}

%changelog
