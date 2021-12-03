import React, { useEffect } from 'react';
import { useHistory, useRouteMatch } from 'react-router';
import { Route, Switch } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';


import {
    Container,
    Section,
    Row,
    AddButton
} from './styled';
import DogList from './DogList';
import AddDog from './AddDog';
import { userDogs } from '../../services';


const DashBoard = () => {
    let { path, url } = useRouteMatch();
    const history = useHistory();
    const dispatch = useDispatch();
    const { id: userId } = useSelector(store => store.account.profile);
    const dogs = useSelector(store => store.dogs.dogs);

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
            <Switch>
                <Route exact path={path}>
                    <DogList dogs={dogs} />
                </Route>
                <Route path={`${path}/add-dog`}>
                    <AddDog />
                </Route>
            </Switch>
        </Container>
    );
};

export default DashBoard;
