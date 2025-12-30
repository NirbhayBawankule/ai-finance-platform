import { Line } from "react-chartjs-2";

export default function Charts({ data }) {
  return (
    <Line
      data={{
        labels: Object.keys(data),
        datasets: [{
          label: "Predicted Expenses",
          data: Object.values(data)
        }]
      }}
    />
  );
}
