Name:		texlive-smart-eqn
Version:	61719
Release:	2
Summary:	Automatic math symbol styling for LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/smart-eqn
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smart-eqn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smart-eqn.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/smart-eqn.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In LaTeX typesetting, one usually needs to use different
variants of a math symbol to clarify the meanings. For example,
in linear algebra literature, it is common to use boldfaced
symbols to represent vectors, and normal symbols to represent
scalars. However, applying these variants by typing \mathbf,
\mathrm commands manually can be daunting. This package aims to
provide an automatic and customizable approach for math symbol
styling which eliminates the need to enter style commands
repeatedly.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/smart-eqn
%{_texmfdistdir}/tex/latex/smart-eqn
%doc %{_texmfdistdir}/doc/latex/smart-eqn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
