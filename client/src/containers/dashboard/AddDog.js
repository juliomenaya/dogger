import React from "react";
import { useHistory } from "react-router";
import { useSelector, useDispatch } from "react-redux";
import { useAlert } from "react-alert";
import { Formik } from "formik";

import { addDog } from "../../reducers/dogs";
import { FormContainer } from "./styled";
import { Input, Select, Button } from "../../components";
import { dogValidation } from "../../validationSchemas";

const AddDog = () => {
    const initialValues = {
        age: '',
        name: '',
        size: 'small'
    };
    const history = useHistory();
    const userProfile = useSelector(store => store.account.profile);
    const dispatch = useDispatch();
    const alert = useAlert();

    return (
        <FormContainer>
            <span>Agrega un lomito</span>
            <Formik
                initialValues={initialValues}
                validationSchema={dogValidation}
                onSubmit={(props) => {
                    props.user_id = userProfile.id;
                    dispatch(addDog(props))
                    .then(({error}) => {
                        if (error) {
                            alert.show(error, { type: 'error'} );
                        } else {
                            alert.show('Lomito creado', { type: 'success'} );
                            history.push('/dashboard');
                        }
                    });
                }}
            >
               {({
                   values,
                   errors,
                   handleChange,
                   handleSubmit,
                   handleBlur,
                   isSubmitting,
                   isValid
               }) => (
                   <>
                        <Input
                            error={errors.name}
                            label='Nombre del lomito'
                            name='name'
                            onBlur={handleBlur}
                            onChange={handleChange}
                            value={values.name}
                        />
                        <Input
                            error={errors.age}
                            label='Años (humanos) del lomito'
                            name='age'
                            onBlur={handleBlur}
                            onChange={handleChange}
                            value={values.age}
                            type='number'
                            min='0'
                        />
                        <Select
                            value={values.size}
                            options={[
                                { value: 'chico', label: 'Chico' },
                                { value: 'mediano', label: 'Mediano' },
                                { value: 'grande', label: 'Grande' }
                            ]}
                            label={'Tamaño'}
                            onChange={handleChange}
                            error={errors.size}
                            name='size'
                        />
                        <Button
                            disabled={!isValid || isSubmitting}
                            onPress={handleSubmit}
                            >
                            Listo
                        </Button>
                   </>
               )} 
            </Formik>
        </FormContainer>
    );
};

export default AddDog;
