#
# spec file for package python-jrnl
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:          python-jrnl
Version:       1.9.8
Release:       0
License:       MIT
Summary:       Collect your thoughts and notes without leaving the command line
Url:           http://maebert.github.io/jrnl/
Group:         Productivity/Office/Organizers
Source0:       jrnl-%{version}.tar.gz
Patch0:        fix-python-dateutil-requirement.patch

BuildRequires: python-setuptools
Requires:      python-dateutil
Requires:      python-keyring
Requires:      python-parsedatetime
Requires:      python-pycrypto
Requires:      python-pytz
Requires:      python-six
Requires:      python-tzlocal
Requires:      python-setuptools

BuildRoot:     %{_tmppath}/%{name}-%{version}-build
BuildArch:     noarch

%description
jrnl is a simple journal application for your command line. Journals are stored
as human readable plain text files - you can put them into a Dropbox folder for
instant syncing and you can be assured that your journal will still be readable
in 2050, when all your fancy iPad journal applications will long be forgotten.

%prep
%setup -q -n jrnl-%{version}
%patch0

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README.md CHANGELOG.md
%{_bindir}/jrnl
%{python_sitelib}/jrnl-%{version}-py%{py_ver}.egg-info
%{python_sitelib}/jrnl

%changelog
