#
# spec file for package git-remote-gcrypt
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           git-remote-gcrypt
Version:        1.2
Release:        0
Summary:        Encrypted git repositories
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            https://spwhitton.name/tech/code/git-remote-gcrypt/
Source:         https://github.com/spwhitton/%{name}/archive/%{version}.tar.gz
BuildRequires:  python-docutils
Requires:       curl
Requires:       git
Requires:       gpg2
Requires:       rsync
BuildArch:      noarch
Suggests:       rclone

%description
This lets git store git repositories in encrypted form.
It supports storing repositories on rsync or sftp servers.
It can also store the encrypted git repository inside a remote git
repository. All the regular git commands like git push and git pull
can be used to operate on such an encrypted repository.

The aim is to provide confidential, authenticated git storage and
collaboration using typical untrusted file hosts or services.

%prep
%setup -q

%build

%install
prefix=%{buildroot}%{_prefix} ./install.sh

%files
%license COPYING
%doc debian/changelog README.rst
%{_bindir}/git-remote-gcrypt
#%{_mandir}/man1/git-remote-gcrypt.1%{ext_man}

%changelog
