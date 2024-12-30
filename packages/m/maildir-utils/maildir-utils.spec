#
# spec file for package maildir-utils
#
# Copyright (c) 2024 SUSE LLC
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


Name:           maildir-utils
Version:        1.12.8
Release:        0
Summary:        Maildir indexer and searcher
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            https://www.djcbsoftware.nl/code/mu/
Source:         https://github.com/djcb/mu/releases/download/v%{version}/mu-%{version}.tar.xz
BuildRequires:  cld2-devel
BuildRequires:  emacs-nox >= 26.3
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmime-3.0) >= 3.0
BuildRequires:  pkgconfig(guile-3.0)
# Optional: for outputting of messages in json
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(xapian-core)

%description
Set of utilities to index and search Maildirs. Upstream name is mu.

%package -n mu4e
Summary:        Emacs-based e-mail client based on the mu e-mail indexer/searcher
Group:          Productivity/Networking/Email/Clients
Requires:       %{name} = %{version}
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
BuildArch:      noarch

%description -n mu4e
mu4e is an emacs-based e-mail client. It is based on the mu e-mail indexer/searcher.

%prep
%setup -q -n mu-%{version}

%build
%meson -Dguile=disabled
%meson_build

%install
%meson_install

%post -n mu4e
%install_info --info-dir=%{_infodir} %{_infodir}/mu4e.info.gz

%preun -n mu4e
%install_info_delete --info-dir=%{_infodir} %{_infodir}/mu4e.info.gz

%files
%doc README.org
%doc %{_datadir}/doc/mu/NEWS.org
%license COPYING
%dir %{_datadir}/doc/mu
%{_bindir}/mu
%{_mandir}/man?/*%{ext_man}

%files -n mu4e
%{_datadir}/doc/mu/mu4e-about.org
%dir %{_datadir}/emacs/site-lisp/mu4e/
%{_datadir}/emacs/site-lisp/mu4e/*.{el,elc}
%{_infodir}/mu4e.info%{?ext_info}

%changelog
