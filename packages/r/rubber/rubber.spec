#
# spec file for package rubber
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rubber
Version:        1.4
Release:        0
Summary:        An automated system for building LaTeX documents
License:        GPL-2.0
Group:          Productivity/Publishing/TeX/Utilities
Url:            https://launchpad.net/rubber
Source:         https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE rubber-makeinfo-unsupported-option.patch badshah400@gmail.com -- older versions of makeinfo does not support the "--info" option, patch it out to fix building on openSUSE <= 13.2.
Patch0:         rubber-makeinfo-unsupported-option.patch
BuildRequires:  makeinfo
BuildRequires:  python-devel >= 2.5
BuildRequires:  texinfo
Requires:       python >= 2.5
Requires:       python-base >= 2.5
Requires:       texlive-latex
Requires(post):  info
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires

%description
Rubber is a building system for LaTeX documents. It is based on a routine that
runs just as many compilations as necessary. The module system provides a
great flexibility that virtually allows support for any package with no user
intervention, as well as pre- and post-processing of the document. The
standard modules currently provide support for bibtex, dvips, dvipdfm, pdftex,
makeindex. A good number of standard packages are supported, including
graphics/graphicx (with automatic conversion between various formats and
Metapost compilation).

%prep
%setup -q
%if 0%{?suse_version} <= 1320
%patch0 -p1
%endif

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --mandir=%{_mandir} --infodir=%{_infodir} --docdir=%{_docdir}/%{name}

%post    
install-info %{_infodir}/rubber.info.gz %{_infodir}/dir

%postun    
install-info --delete %{_infodir}/rubber.info.gz %{_infodir}/dir

%files
%defattr(-,root,root)
%doc COPYING NEWS README
%{_bindir}/rubber
%{_bindir}/rubber-pipe
%{_bindir}/rubber-info
%{python_sitelib}/rubber/
%{python_sitelib}/rubber-%{version}-py%{py_ver}.egg-info
%{_mandir}/man1/rubber-info.1*
%{_mandir}/man1/rubber-pipe.1*
%{_mandir}/man1/rubber.1*
%{_infodir}/rubber.info.gz
%{_mandir}/fr/man1/*.gz
%{_docdir}/%{name}/

%changelog
