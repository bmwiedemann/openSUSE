#
# spec file for package python-tensorboard
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


# sync with tensorflow2
%define pythons python3
Name:           python-tensorboard
Version:        2.6.0
Release:        0
Summary:        TensorFlow's Visualization Toolkit
License:        Apache-2.0
URL:            https://github.com/tensorflow/tensorboard
# no sdist. Use the pure wheel. It is much easier than a Bazel build
Source0:        https://files.pythonhosted.org/packages/py3/t/tensorboard/tensorboard-%{version}-py3-none-any.whl
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-Markdown >= 2.6.8
Requires:       python-Werkzeug >= 0.11.15
Requires:       python-abseil >= 0.4
Requires:       python-google-auth >= 1.6.3
Requires:       python-google-auth-oauthlib >= 0.4.1
Requires:       python-grpcio >= 1.24.3
Requires:       python-numpy >= 1.12.0
Requires:       python-protobuf >= 3.6.0
Requires:       python-requests >= 2.21.0
Recommends:     python-tensorboard-data-server >= 0.6.0
Recommends:     python-tensorboard-plugin-wit >= 1.6.0
BuildArch:      noarch
%python_subpackages

%description
TensorBoard is a suite of web applications for inspecting and understanding
your TensorFlow runs and graphs.

TensorBoard is designed to run entirely offline, without requiring any access
to the Internet. For instance, this may be on your local machine, behind a
corporate firewall, or in a datacenter.

%package cmd
Summary:       TensorFlow's Visualization Toolkit -- standalone command
# tensorflow2 also provides the entrypoint
Conflicts:     tensorflow2
Requires:      %{name} = %{version}

%description cmd
TensorBoard is a suite of web applications for inspecting and understanding
your TensorFlow runs and graphs.

TensorBoard is designed to run entirely offline, without requiring any access
to the Internet. For instance, this may be on your local machine, behind a
corporate firewall, or in a datacenter.

This package provides the command if it is meant to be used without tensorflow2

%prep
%setup -q -c tensorboard-%{version} -T

%build
# deprecated usage of wheel in cwd for pyproject_install due to old python-rpm-macros on Leap 15.X
cp %{SOURCE0} .

%install
%pyproject_install
cp %{buildroot}%{python3_sitelib}/tensorboard-%{version}.dist-info/LICENSE .
%{python_expand #
%fdupes %{buildroot}%{$python_sitelib}
chmod a-x %{buildroot}%{$python_sitelib}/tensorboard/webfiles.zip \
          %{buildroot}%{$python_sitelib}/tensorboard/plugins/projector/tf_projector_plugin/projector_binary.{html,js}
}

#%%check
# no testsuite without bazel

%files %{python_files}
%license LICENSE
%{python_sitelib}/tensorboard
%{python_sitelib}/tensorboard-%{version}.dist-info

%files %{python_files cmd}
%license LICENSE
%{_bindir}/tensorboard

%changelog
