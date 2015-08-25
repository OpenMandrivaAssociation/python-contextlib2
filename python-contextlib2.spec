%define modname contextlib2

Name:               python-contextlib2
Version:            0.4.0
Release:            1
Summary:            Backports and enhancements for the contextlib module
Group:              Development/Python
License:            Python
URL:                http://pypi.python.org/pypi/contextlib2
Source0:            https://pypi.python.org/packages/source/c/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:          noarch
BuildRequires:      python-devel
BuildRequires:      python3-devel

%description
contextlib2 is a backport of the standard library's contextlib module to
earlier Python versions.

It also serves as a real world proving ground for possible future
enhancements to the standard library version.

%package -n python3-contextlib2
Summary:            Backports and enhancements for the contextlib module
Group:              Development/Python

%description -n python3-contextlib2
contextlib2 is a backport of the standard library's contextlib module to
earlier Python versions.

It also serves as a real world proving ground for possible future
enhancements to the standard library version.

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info
rm -rf %{py3dir}
cp -a . %{py3dir}

%build
python2 setup.py build
pushd %{py3dir}
python3 setup.py build
popd

%install
pushd %{py3dir}
python3 setup.py install -O1 --skip-build --root=%{buildroot}
popd
python2 setup.py install -O1 --skip-build --root=%{buildroot}

%check
python2 test_contextlib2.py
pushd %{py3dir}
python3 test_contextlib2.py
popd

%files
%doc README.txt VERSION.txt NEWS.rst LICENSE.txt
%{py_puresitedir}/%{modname}.py*
%{py_puresitedir}/%{modname}-%{version}*

%files -n python3-contextlib2
%doc README.txt VERSION.txt NEWS.rst LICENSE.txt
%{py3_puresitedir}/%{modname}.py*
%{py3_puresitedir}/%{modname}-%{version}-*

