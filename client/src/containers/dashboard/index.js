import React, { useEffect } from 'react';
import { useHistory, useRouteMatch } from 'react-router';
import { Route } from 'react-router-dom';
import { Formik } from 'formik';
import { useSelector, useDispatch } from 'react-redux';
import { useAlert } from 'react-alert';


import { Container, Section, Row, AddButton, FormContainer } from './styled';
import { Select } from '../../components';
import { Input } from '../../components';
import { Button } from '../../components';
import { dogValidation } from '../../validationSchemas';
import { addDog } from '../../reducers/dogs';
import { userDogs } from '../../services';


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

const DashBoard = () => {
    let { path, url } = useRouteMatch();
    const history = useHistory();
    const dispatch = useDispatch();
    const { id: userId } = useSelector(store => store.account.profile);
    const dogs = useSelector(store => store.dogs.dogs);
    console.log('A ver mis perros ', dogs)

    useEffect(() => {
        const getDogs = async () => {
            let response = await userDogs(userId);
            dispatch({ type: 'SET_DOGS', payload: response.data });
        };
        getDogs();
    }, [userId, dispatch]);

    return (
        <Container>
            <Row>
                <Section>My dogs</Section>
                <AddButton onClick={() => history.push(`${url}/add-dog`)}>+</AddButton>
            </Row>
            
            <Route path={`${path}/add-dog`}>
                <AddDog />
            </Route>
        </Container>
    );
};

export default DashBoard;
