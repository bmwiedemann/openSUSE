#
# spec file for package CastXML
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


Name:           CastXML
Version:        0.5.1
Release:        0
Summary:        C-family Abstract Syntax Tree XML Output
License:        Apache-2.0
URL:            https://github.com/CastXML/CastXML
Source0:        https://github.com/CastXML/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python3-Sphinx
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)

%description
CastXML is a C-family abstract syntax tree XML output tool.

%package devel
Summary:        C-family Abstract Syntax Tree XML Output

%description devel
CastXML is a C-family abstract syntax tree XML output tool.

%prep
%autosetup -p1

%build
%cmake -DCastXML_INSTALL_MAN_DIR:PATH=%{_mandir} \
       -DCastXML_INSTALL_DOC_DIR:PATH=%{_docdir}/%{name} \
       -DCLANG_LINK_CLANG_DYLIB:BOOL=ON \
       -DBUILD_TESTING:BOOL=ON \
       -DSPHINX_HTML:BOOL=ON \
       -DSPHINX_MAN:BOOL=ON

%cmake_build

%install
%cmake_install

# REMOVE FILES TO BE INSTALLED USING %%doc OR %%license
rm %{buildroot}%{_docdir}/%{name}/LICENSE

%fdupes %{buildroot}%{_datadir}/castxml/clang/include/

%check
%ctest

%files devel
%license LICENSE
%{_bindir}/castxml
%{_mandir}/man1/castxml.1%{?ext_man}
%{_datadir}/castxml/
%doc %{_docdir}/%{name}

%changelog
