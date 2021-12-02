import React from "react";

import { InputContainer, Label } from "../input/styled";
import { ElementSelect } from "./styled";

const Select = ({ error, label, name, onChange, value, options }) => {    
  return (
    <InputContainer>
      <Label>{label}</Label>
      <ElementSelect
        name={name}
        error={error}
        onChange={onChange}
        value={value}
      >
          {options.map(o => <option value={o.value}>{o.label}</option>)}
      </ElementSelect>
    </InputContainer>
  );
};

export default Select;
