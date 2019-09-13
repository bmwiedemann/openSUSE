#
# spec file for package py-fishcrypt
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


%global commit 43554b1ae4887791ae7ebd76f57c84ce0296d1cb
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           py-fishcrypt
Version:        5.31
Release:        0
Summary:        FiSH/Mircryption-compatible encryption for XChat/HexChat
License:        BSD-3-Clause and GPL-2.0+ or Artistic-1.0
Group:          Productivity/Networking/IRC
Url:            https://github.com/fladd/py-fishcrypt
Source0:        %{name}-%{version}+git-43554b1.tar.bz2
Source1:        %{name}-rpmlintrc
Source2:        generate-service-file.sh
Requires:       python
Requires:       python-SocksiPy
Requires:       python-pycrypto
BuildRequires:  dos2unix
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FiSH/Mircryption-compatible encryption for XChat/HexChat.

    Encrypt/decrypt private conversations
    Encrypt/decrypt channel conversations
    Choose between ECB and CBC
    Automatic DH key exchange (private conversations only)

To make FiSH work with py-fishcrypt please do symlink as user

    su user

    For HexChat

    ln -sf %{_datadir}/%{name}/*.py ~/.config/hexchat/addons/


    For XChat

    ln -sf %{_datadir}/%{name}/*.py ~/.xchat2/

    exit

%prep
%setup -q -n %{name}-%{version}+git-%{shortcommit}

# Convert to unix line end
find . -name "*.py" -exec dos2unix "{}" "+"

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -Dm 0555 *.py %{buildroot}%{_datadir}/%{name}

%files
%defattr(-,root,root,-)
%doc README.md
%{_datadir}/%{name}

%changelog
