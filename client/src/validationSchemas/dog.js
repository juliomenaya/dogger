import * as Yup from 'yup';

const dogValidation = Yup.object().shape({
    name: Yup.string()
        .required('Tu lomito debe estar bautizado'),
    age: Yup.number()
        .positive()
        .integer()
        .required('Debe tener al menos un año para poder salir a la calle'),
    size: Yup.string()
        .required('Campo requerido')
});

export default dogValidation;
