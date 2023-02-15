# Library of Congress

*A simply digitial bookstore for collecting books and adding to the global source of knowledge.*

**Languages:** Django, Python, HTML, CSS
  
---

## Getting Started

[Find the website here](http://libraryofcongress.herokuapp.com)

Visitors are first prompted to create an account (or login, if they have it). After logging in, visitors have the options to add authors and books via different forms.

![Screenshot showing home page](https://i.imgur.com/5jSBOHZ.png)

Books default to having no author. However, if a user has created one or more authors, they will be prompted to add an author from the author list shown below the books detail page.

![Screenshot showing add author feature](https://i.imgur.com/ohLHZDP.png)

---

## Minutia

This website uses the professional styling system Materialize. While a few tweaks to fine tune the user experience were made, this site stays true to the Materialize styling.

Users can add as many books and authors as they wish, though they are limited to adding one author per book. Multiple books can be written by the same author. Associating an author to a book is permanent. 

---

## Future Enhancements

**ISBN API Connection**

With the OpenLibrary API, as user would only need to submit the book's ISBN and our system can get the rest of the information via API, saving the user time and improving the UX.

**3D books**

With the right CSS, books can be rendered as a lightweight 3d object in the browser with a simple animation, adding a sense of fun and playfullness to the UX as visitors see the books come to life just that little bit.

**Default booklist**

This website is blank upon arrival, but as it's representative of the Library of Congress, I hope to add a series of default books to prepopulate the website for visitors to see.

---

By Alex Westerlund
