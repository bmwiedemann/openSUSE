#
# spec file for package CastXML
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.3.4
Release:        0
Summary:        C-family Abstract Syntax Tree XML Output
License:        Apache-2.0
URL:            https://github.com/CastXML/CastXML
Source:         https://github.com/CastXML/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-Sphinx

%description
CastXML is a C-family abstract syntax tree XML output tool.

%package devel
Summary:        C-family Abstract Syntax Tree XML Output

%description devel
CastXML is a C-family abstract syntax tree XML output tool.

%prep
%setup -q

%build
# FOR LLVM/CLANG >= 10 CLANG_LINK_CLANG_DYLIB NEEDS TO BE SET TO ON TO COMPILE
# AGAINST LLVM/CLAN DYNAMIC LIBS
%cmake -DCastXML_INSTALL_MAN_DIR:PATH=%{_mandir} \
       -DCastXML_INSTALL_DOC_DIR:PATH=%{_docdir}/%{name} \
%if 0%{?suse_version} >= 1550
       -DCLANG_LINK_CLANG_DYLIB:BOOL=ON \
%endif
       -DSPHINX_HTML:BOOL=ON \
       -DSPHINX_MAN:BOOL=ON

%cmake_build

%install
%cmake_install

# REMOVE FILES TO BE INSTALLED USING %%doc OR %%license
rm %{buildroot}%{_docdir}/%{name}/LICENSE

%files devel
%license LICENSE
%{_bindir}/castxml
%{_mandir}/man1/castxml.1%{?ext_man}
%{_datadir}/castxml/
%doc %{_docdir}/%{name}

%changelog
