# Hugo on openSUSE MicroOS, Tumbleweed or other container hosts

Hugo is one of the most popular open-source static site generators. With its amazing speed and flexibility, Hugo makes building websites fun again.

## Usage

Pull the image:

```sh
podman pull registry.opensuse.org/opensuse/hugo
```

Create new Hugo site/blog:

```sh
podman run -p 1313:1313 -v $PWD/blog:/src -it registry.opensuse.org/opensuse/hugo new blog .
```

This will create Hugo site structure in `$PWD/blog`.

Start development server:

```sh
podman run -p 1313:1313 -v $PWD/blog:/src -it registry.opensuse.org/opensuse/hugo server
```

Development server will be available at [http://localhost:1313/](http://localhost:1313/).

Build static site:

```sh
podman run -p 1313:1313 -v $PWD/blog:/src -it registry.opensuse.org/opensuse/hugo --gc -d public
```

The static site will be in `$PWD/blog/public`.

## More Information

 * [Hugo Project](https://gohugo.io/)
 * [Hugo Documentation](https://gohugo.io/documentation/)
 * [Hugo Themes](https://themes.gohugo.io/)
