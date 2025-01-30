#
# spec file for package python-imapdedup
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

%if 0%{?suse_version} >= 1699
%define pythons python3
%else
%{?sle15_python_module_pythons}
%endif
Name:            python-imapdedup
Version:         1.2
Release:         0
Summary:         IMAP de-duplication tool
License:         GPL-2.0-only
URL:             https://github.com/quentinsf/IMAPdedup
Source:          https://files.pythonhosted.org/packages/source/i/imapdedup/imapdedup-%{version}.tar.gz
BuildRequires:   python-rpm-macros
BuildRequires:   %{python_module hatchling}
BuildRequires:   %{python_module pip}
BuildRequires:   fdupes
Requires(post):  update-alternatives
Requires(postun): update-alternatives
BuildArch:       noarch
%python_subpackages

%description
A duplicate email message remover

IMAPdedup is a command-line utility that looks for duplicate messages in a set
of IMAP mailboxes and tidies up all but the first copy of any duplicates found.

To be more exact, it *marks* the second and later occurrences of a message as
'deleted' on the server.   Exactly what that does in your environment will
depend on your mail server and your mail client.

Some mail clients will let you still view such messages *in situ*, so you can
take a look at what's happened before 'compacting' the mailbox.  Sometimes
deleted messages appear in a 'Trash' folder.  Sometimes they are hidden and can
be displayed and un-deleted if wanted, until they are purged.

Whatever your system does, you will usually have the option to see what has
been deleted, and to recover it if needed, using your email program, after
running this script.  (If your server purges the deleted messages
automatically, you may be able to prevent this with the `--no-close` option.)
There is also a 'dry-run' option so you can check what might happen before
doing anything scary.

%prep
%autosetup -p1 -n imapdedup-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
sed -i 's/env python3/python3/' %{buildroot}%{_bindir}/imapdedup
%python_expand sed -i 's/env python3/python3/' %{buildroot}%{$python_sitelib}/imapdedup/imapdedup.py
%python_clone -a %{buildroot}%{_bindir}/imapdedup
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative imapdedup

%postun
%python_uninstall_alternative imapdedup

%files %{python_files}
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/imapdedup
%{python_sitelib}/imapdedup
%{python_sitelib}/imapdedup-%{version}.dist-info

%changelog
