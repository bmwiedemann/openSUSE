#
# spec file for package rubber
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


Name:           rubber
Version:        1.5.1
Release:        0
Summary:        An automated system for building LaTeX documents
License:        GPL-2.0-only
Group:          Productivity/Publishing/TeX/Utilities
URL:            https://launchpad.net/rubber
Source:         https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  makeinfo
BuildRequires:  python3-devel
BuildRequires:  texinfo
Requires:       python3
Requires:       texlive-latex
Requires(post): info
BuildArch:      noarch

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

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --mandir=%{_mandir} --infodir=%{_infodir} --docdir=%{_docdir}/%{name}

%fdupes %{buildroot}%{python3_sitelib}/rubber/

%post
install-info %{_infodir}/rubber.info.gz %{_infodir}/dir

%postun
install-info --delete %{_infodir}/rubber.info.gz %{_infodir}/dir

%files
%doc NEWS README
%license COPYING
%{_bindir}/rubber
%{_bindir}/rubber-pipe
%{_bindir}/rubber-info
%{python3_sitelib}/rubber/
%{python3_sitelib}/rubber-%{version}-py%{py3_ver}.egg-info
%{_mandir}/man1/rubber-info.1%{?ext_man}
%{_mandir}/man1/rubber-pipe.1%{?ext_man}
%{_mandir}/man1/rubber.1%{?ext_man}
%{_infodir}/rubber.info%{?ext_info}
%{_mandir}/fr/man1/*.gz
%{_docdir}/%{name}/

%changelog
