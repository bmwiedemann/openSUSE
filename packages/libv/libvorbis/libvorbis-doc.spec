#
# spec file for package libvorbis-doc
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


%if 0%{?suse_version} > 1320
%define build_docs 1
%else
%define build_docs 0
%endif

Name:           libvorbis-doc
Version:        1.3.7
Release:        0
Summary:        Documentation of Ogg/Vorbis library
License:        BSD-3-Clause
Group:          Documentation/Other
URL:            https://www.vorbis.com/
Source:         https://downloads.xiph.org/releases/vorbis/libvorbis-%{version}.tar.xz
Source1:        https://downloads.xiph.org/releases/vorbis/libvorbis-%{version}.tar.xz.asc
Source99:       libvorbis.keyring
Patch1:         libvorbis-lib64.dif
Patch2:         libvorbis-m4.dif
Patch12:        vorbis-ocloexec.patch
BuildRequires:  fdupes
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
%if %build_docs
BuildRequires:  doxygen
BuildRequires:  texlive-babel-english
BuildRequires:  texlive-latex
BuildRequires:  texlive-tex4ht
BuildRequires:  tex(a4wide.sty)
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(csquotes.sty)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(grffile.sty)
BuildRequires:  tex(parskip.sty)
BuildRequires:  tex(ulem.sty)
BuildRequires:  tex(underscore.sty)
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains documents for Ogg/Vorbis library, including the
API reference.

%prep
%setup -q -n libvorbis-%{version}
%patch2
# %%patch5 -p1
if [ "%{_lib}" == "lib64" ]; then
%patch1
fi
%patch12

%build
autoreconf -fiv
%configure \
%if %build_docs
	--enable-docs \
%endif
	--disable-examples \
	--disable-static
# parallel-build of docs may fail
make -C doc
# we don't build anything but docs

%install
make -C doc DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/libvorbis-* %{buildroot}%{_docdir}/%{name}
# remove unneeded files
find %{buildroot}%{_docdir}/ -empty -delete
%fdupes -s %{buildroot}%{_docdir}

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}

%changelog
