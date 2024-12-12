import React from "react";

const Accesibilidad = () => {
    const toggleClass = (className) => document.body.classList.toggle(className);

    return (
        <div>
            <button onClick={() => toggleClass("alto-contraste")}>Alto Contraste</button>
            <button onClick={() => toggleClass("escala-grises")}>Escala de Grises</button>
            <button onClick={() => window.location.reload()}>Restablecer</button>
        </div>
    );
};

export default Accesibilidad;
