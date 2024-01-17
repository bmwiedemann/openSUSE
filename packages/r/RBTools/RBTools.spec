#
# spec file for package rbtools
#
# Copyright (c) 2021 SUSE LLC
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


Name:           RBTools
Version:        1.0.3
Release:        0
Summary:        Command line tools for interacting with review board
License:        MIT
Group:          Development/Tools/Other
URL:            https://www.reviewboard.org
Source:         https://downloads.reviewboard.org/releases/RBTools/1.0/RBTools-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-setuptools
Requires:       python3-colorama
Requires:       python3-setuptools
Requires:       python3-six >= 1.8.0
Requires:       python3-texttable
Requires:       python3-tqdm
BuildArch:      noarch

%description
rbtools is a set of client tools to use with Review Board.
This consists of the following officially supported tools:

    * post-review
      - Create and update review requests based on changes in a local tree.
    * rbt
      - Execute a number of useful sub-commands to interact with local source
        code repositories and Review Board.
    * Python API Client
      - Python bindings to simplify interaction with the the Review Board
        Web API.

There are also some user-contributed scripts and application plugins in the
contrib directory. See the associated README files for more information.

%prep
%autosetup
sed -ie "/^#\!\/usr\/bin\/env/d" rbtools/utils/appdirs.py

%build
%python3_build

%install
%python3_install
%fdupes -s %{buildroot}%{python3_sitelib}

%files
%license COPYING
%doc README.md
%{_bindir}/rbt
%{python3_sitelib}/rbtools*
%{python3_sitelib}/RBTools-%{version}-py%{py3_ver}.egg-info

%changelog
