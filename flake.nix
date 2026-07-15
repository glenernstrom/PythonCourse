{
  description = "Python development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";

      pkgs = import nixpkgs {
        inherit system;
      };

      python = pkgs.python314Full;
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          python
          pkgs.thonny
        ];

        shellHook = ''
          export PS1="[(python-dev) | \u@\h \W]\$ "

          echo
          echo "Python Development Environment"
          echo "------------------------------"
          python --version
          echo
          echo "Available commands:"
          echo "  python"
          echo "  idle3"
          echo "  thonny"
          echo
        '';
      };
    };
}
