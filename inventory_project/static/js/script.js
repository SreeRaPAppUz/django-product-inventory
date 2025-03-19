document.addEventListener("DOMContentLoaded", function () {
    const apiBaseUrl = "/api/products/";
    
    // Fetch and display all products
    function loadProducts() {
        fetch(apiBaseUrl)
            .then(response => response.json())
            .then(data => {
                let productTable = document.getElementById("productTable");
                productTable.innerHTML = "";
                
                data.forEach(product => {
                    productTable.innerHTML += `
                        <tr id="product-${product.id}">
                            <td>${product.name}</td>
                            <td><input type="number" class="form-control update-price" data-id="${product.id}" value="${product.price}" step="0.01"></td>
                            <td><input type="number" class="form-control update-stock" data-id="${product.id}" value="${product.stock}"></td>
                            <td>
                                <button class="btn btn-success update-product" data-id="${product.id}">Update</button>
                                <button class="btn btn-danger delete-product" data-id="${product.id}">Delete</button>
                            </td>
                        </tr>`;
                });

                attachEventListeners(); // Attach event listeners to buttons
            })
            .catch(error => console.error("Error fetching products:", error));
    }

    // Add new product
    document.getElementById("addProductForm").addEventListener("submit", function (event) {
        event.preventDefault();

        let formData = new FormData(this);
        let productData = Object.fromEntries(formData.entries());

        fetch(apiBaseUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
            body: JSON.stringify(productData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.id) {
                loadProducts();
                this.reset(); // Clear form after adding
            }
        })
        .catch(error => console.error("Error adding product:", error));
    });

    // Update product
    function updateProduct(id) {
        let price = document.querySelector(`.update-price[data-id='${id}']`).value;
        let stock = document.querySelector(`.update-stock[data-id='${id}']`).value;

        fetch(`${apiBaseUrl}${id}/`, {
            method: "PUT",
            headers: { "Content-Type": "application/json", "X-CSRFToken": getCSRFToken() },
            body: JSON.stringify({ price, stock })
        })
        .then(response => response.json())
        .then(() => alert("Product updated successfully!"))
        .catch(error => console.error("Error updating product:", error));
    }

    // Delete product
    function deleteProduct(id) {
        if (confirm("Are you sure?")) {
            fetch(`${apiBaseUrl}${id}/`, {
                method: "DELETE",
                headers: { "X-CSRFToken": getCSRFToken() }
            })
            .then(() => document.getElementById(`product-${id}`).remove())
            .catch(error => console.error("Error deleting product:", error));
        }
    }

    // Attach event listeners to update and delete buttons
    function attachEventListeners() {
        document.querySelectorAll(".update-product").forEach(button => {
            button.addEventListener("click", function () {
                updateProduct(this.dataset.id);
            });
        });

        document.querySelectorAll(".delete-product").forEach(button => {
            button.addEventListener("click", function () {
                deleteProduct(this.dataset.id);
            });
        });
    }

    // Helper function to get CSRF token
    function getCSRFToken() {
        return document.querySelector("[name=csrfmiddlewaretoken]").value;
    }

    // Initial load of products
    loadProducts();
});
